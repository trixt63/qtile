# GNOME Keyring, PAM and gcr-prompter under qtile

Why opening Obsidian could "freeze" the desktop, how the pieces fit together,
and what was changed to fix it (Oct 2026).

## Symptom

- Open Obsidian (Flatpak) some time after logging in.
- The pointer still moves, but clicks and keys do nothing.
- On Oct 14 the cause was visible: an "unlock keyring" password dialog was
  stacked **behind** the Obsidian window.
- The system wasn't hung; the logs kept running and the kernel log was clean.

## 1. The keyring: an encrypted password file

Apps need to store secrets: Obsidian's encryption key, browser passwords, Wi-Fi
passwords, tokens. Instead of each app storing them in plain text, they share one
encrypted file:

```
~/.local/share/keyrings/login.keyring
```

It is encrypted with a password, normally the same as the login password.

- **Locked**: still encrypted on disk; nobody can read it.
- **Unlocked**: decrypted into memory; apps can get their secrets without asking.

## 2. gnome-keyring-daemon: the program that holds it open

`gnome-keyring-daemon` loads the keyring and serves secrets to apps. Apps talk to
it over **D-Bus** (the desktop's message bus) through a standard interface called
the **Secret Service** (`org.freedesktop.secrets`).

When Obsidian starts, Electron asks the Secret Service for its stored key. The
Flatpak is allowed to do that by its `org.freedesktop.secrets=talk` permission.

If no daemon is answering, D-Bus **starts one automatically** ("D-Bus activation").
That detail matters below.

## 3. PAM: how login unlocks it without asking

**PAM** (Pluggable Authentication Modules) is the set of plugins that runs on every
login: LightDM, `sudo`, a text console, and so on. Each login program has a list of
modules to run. `/etc/pam.d/common-auth` and `/etc/pam.d/common-session` include
`pam_gnome_keyring.so`, set to run only for LightDM, GDM and similar login screens:

```
auth    optional  pam_gnome_keyring.so  only_if=gdm,gdm-password,lxdm,lightdm,mdm,sddm
session optional  pam_gnome_keyring.so  auto_start only_if=gdm,gdm-password,lxdm,lightdm,mdm,sddm
```

When the password is typed into LightDM, it does two things:

| PAM phase | What `pam_gnome_keyring` does | Log line (system journal) |
|---|---|---|
| **auth** (checking the password) | Remembers the password for a moment | `gkr-pam: stashed password to try later in open session` |
| **session** (starting the session) | Starts `gnome-keyring-daemon --daemonize --login` and unlocks the keyring with that password | `gkr-pam: gnome-keyring-daemon started properly and unlocked keyring` |

So:

- The keyring password must match the login password for this to work.
- Auto-login can't unlock it, because there is no password to reuse.

## 4. "Attaching": the step qtile was missing

The daemon PAM starts is deliberately minimal. The desktop session is then
expected to run:

```
gnome-keyring-daemon --start --components=secrets
```

That doesn't start a second keyring. It finds the daemon PAM started
(`discover_other_daemon: 1`), enables the Secret Service part and connects it to
the session.

GNOME and XFCE do this automatically via
`/etc/xdg/autostart/gnome-keyring-secrets.desktop`. That file says
`OnlyShowIn=GNOME;Unity;MATE;XFCE`, and `XDG_CURRENT_DESKTOP=qtile`, so under qtile
it never ran.

Without that step, the logs show the daemon PAM started had disappeared whenever
the first secret request came more than a minute or two after login:

| Login | First keyring request | Gap | Result |
|---|---|---|---|
| Oct 10 15:14 | 15:14:50 | seconds | worked |
| Oct 11 10:12 | 11:00:22 | 48 min | daemon gone, prompt |
| Oct 12 23:07:33 | 23:07:40 | 7 s | worked |
| Oct 13 22:54:52 | 22:57:13 | 2 min 20 s | daemon gone, hidden prompt |
| Oct 13 23:02:47 | 23:03:37 | 50 s | worked |
| Oct 14 21:42 | 22:07:30 | 25 min | daemon gone, prompt behind Obsidian |

What happens when it's gone:

1. Obsidian asks the Secret Service for its key.
2. Nothing answers, so D-Bus activation starts a **brand-new** daemon.
3. That daemon looks for the one PAM started and finds nothing
   (`couldn't access control socket` / `discover_other_daemon: 0`).
4. The new daemon never saw the password, so the keyring is **locked** and it
   has to ask for it.

The exact reason the daemon PAM started disappears is not recorded anywhere in the
logs (no crash dump, no exit message).

## 5. gcr and gcr-prompter: the password dialog

**gcr** is a GNOME library for cryptography and certificates. It includes
**`gcr-prompter`**, a small separate program whose only job is to draw
"Enter password to unlock your login keyring" dialogs for the keyring daemon.

On X11, **any program can read every keystroke** sent to any other window. To stop
another app from snooping on the keyring password, gcr-prompter **grabs** the
keyboard and mouse: while the dialog is open, all input goes only to it. That's a
normal security measure.

It becomes a trap when the dialog is somewhere you can't see. The pointer still
moves (X draws the cursor itself), but every click and keypress goes to an
invisible dialog, which looks exactly like a freeze.

## The whole chain

```
LightDM login ──PAM──▶ daemon started + keyring unlocked
                          │
   (qtile never "attaches"; ~1–2 min later the daemon is gone)
                          │
Obsidian asks for secret ─▶ new, locked daemon ─▶ gcr-prompter grabs input
                                                      │
                                    dialog behind Obsidian ─▶ "frozen"
```

## Fixes in this config

1. **`autostart.sh`**: runs the attach step at login, so a locked keyring and its
   prompt shouldn't happen:

   ```sh
   gnome-keyring-daemon --start --components=secrets &
   ```

2. **`modules/hooks.py`**: if a prompt appears anyway, qtile keeps it above other
   windows, brings it to the front and focuses it:

   ```python
   @hook.subscribe.client_managed
   def raise_keyring_prompt(window):
       if "gcr-prompter" in (window.get_wm_class() or []):
           window.keep_above(enable=True)
           window.bring_to_front()
           window.focus()
   ```

## If it locks up anyway

1. Press **Ctrl+Alt+F3** to get a text console. Switching consoles is handled by
   the X server itself, which a dialog's input grab can't block.
2. Log in and run `pkill gcr-prompter`. This closes the dialog and releases the grab.
3. Press **Ctrl+Alt+F7** (or F2) to go back to the desktop.

## Useful checks

```sh
# Both should be listed: the --login one (from PAM) and the --start one (attached)
pgrep -a gnome-keyring

# A prompt that started but never completed = an input grab you can't see
journalctl --user -b | grep -E 'gcr-prompter.*(starting|completed) password prompt'

# Did the attach find the login daemon? 1 = yes, 0 = started a fresh locked one
journalctl --user -b | grep discover_other_daemon
```
