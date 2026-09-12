#!/bin/sh

# Tell systemd --user about the graphical session, so units with
# Requisite=graphical-session.target (xdg-desktop-portal) can start.
# Without this, Flatpak apps cannot open links/files via the portal.
export XDG_CURRENT_DESKTOP=qtile
systemctl --user set-environment XDG_CURRENT_DESKTOP=qtile
# systemctl --user import-environment DISPLAY XAUTHORITY
systemctl --user start qtile-session.target

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
#Discord
discord &
#Power management
xfce4-power-manager &
#Bluetooth manager
blueman-applet &
#Mail client
thunderbird &
#Dictionary
goldendict &
# network manager
nm-applet
#Rclone
#rclone mount --daemon "Google Drive:" /home/trinhtung/Google_Drive/xuantung.trinh.63/ &
# sleep 1 && xkbcomp /home/trinhtung/.config/Xkeymap $DISPLAY &
# killall xcape &
# xcape -e 'Control_L=Escape;'
