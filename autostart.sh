#!/bin/sh

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
