#!/bin/sh

#Policy-kit
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
#input method
ibus-daemon &
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
#Mail client
thunderbird &
#Discord
flatpak run com.discordapp.Discord &
#Dictionary
goldendict
