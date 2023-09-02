#!/bin/sh

#Policy-kit
/usr/libexec/polkit-gnome-authentication-agent-1 &

#Notification (only needed on Tumbleweed so far)
/usr/libexec/xfce4/notifyd/xfce4-notifyd & 

#Settings (only needed on Tumbleweed so far)
xfsettingsd &

#input method
# ibus-daemon &
fcitx5 &

# network manager
nm-applet &
#Power management
xfce4-power-manager &
#Bluetooth manager
blueman-applet &
#Clipboard
xfce4-clipman &
#Redshift for eyestrain
redshift-gtk &
#Discord
flatpak run com.discordapp.Discord &
#Mail client
thunderbird &
#Dictionary
goldendict &
#Rclone
rclone mount --daemon "Google Drive:" /home/xuantung/Google_Drive/xuantung.trinh.63/
