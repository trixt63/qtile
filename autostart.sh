#!/bin/sh

# Tell systemd --user about the graphical session, so units with
# Requisite=graphical-session.target (xdg-desktop-portal) can start.
# Without this, Flatpak apps cannot open links/files via the portal.
# This fix needs ~/.config/systemd/user/qtile-session.target and
# ~/.config/xdg-desktop-portal/portals.conf.
# Refer to https://github.com/trixt63/Linux-configurations/commit/67ace6 for more information.
systemctl --user start qtile-session.target

# Leave XDG_CURRENT_DESKTOP unset. If it is set, rofi applies OnlyShowIn and hides
# XFCE apps (settings, Power Manager). The portal doesn't need it: portals.conf
# selects the backend.
# export XDG_CURRENT_DESKTOP=qtile
# systemctl --user set-environment XDG_CURRENT_DESKTOP=qtile
# systemctl --user import-environment DISPLAY XAUTHORITY

# Attach to the keyring that PAM unlocked at login. Under GNOME/XFCE the
# gnome-keyring-secrets autostart entry does this, but it skips qtile; without it
# the login daemon is gone later and apps get an "unlock keyring" prompt.
gnome-keyring-daemon --start --components=secrets &

#Policy-kit
/usr/libexec/polkit-gnome-authentication-agent-1 &
#Notification (only needed on Tumbleweed so far)
/usr/libexec/xfce4/notifyd/xfce4-notifyd & 
#Settings (only needed on Tumbleweed so far)
xfsettingsd &
#input method
fcitx5 &
#Clipboard
xfce4-clipman &
#Redshift for eyestrain
redshift-gtk &
#Power management
xfce4-power-manager &
#Screensaver
xfce4-screensaver &
#Bluetooth manager
blueman-applet &
#Mail client
thunderbird &
#Dictionary
goldendict &
# network manager
nm-applet &

flatpak run com.spotify.Client
#Rclone
#rclone mount --daemon "Google Drive:" /home/trinhtung/Google_Drive/xuantung.trinh.63/ &
# sleep 1 && xkbcomp /home/trinhtung/.config/Xkeymap $DISPLAY &
# killall xcape &
# xcape -e 'Control_L=Escape;'
