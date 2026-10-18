import subprocess
import os

from libqtile import hook
from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()


# Auto start
@hook.subscribe.startup_once
def autostart():
    _autostart = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([_autostart])


# Auto restart
@hook.subscribe.startup
def autorestart():
    _autorestart = os.path.expanduser('~/.config/qtile/autorestart.sh')
    subprocess.Popen([_autorestart])


# Keyring password prompt grabs keyboard and mouse; keep it on top so it can't hide behind other windows
@hook.subscribe.client_managed
def raise_keyring_prompt(window):
    if "gcr-prompter" in (window.get_wm_class() or []):
        window.keep_above(enable=True)
        window.bring_to_front()
        window.focus()
