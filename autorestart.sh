#!/bin/sh

#Input method
ibus restart &
#Wallpaper
# feh --bg-fill /home/xuantung/Pictures/wallpapers/nord-wallpapers/debian-galaxy.png
feh --bg-fill /home/xuantung/Pictures/wallpapers/nord-wallpapers/ign_sunGarden.png
#Compositor
picom &
#X keyboard extension
xkbcomp $HOME/.config/xkb/Xkeymap $DISPLAY &
bash $HOME/.config/xkb/xcape.sh &
#Mouse scrolling speed
killall imwheel &
imwheel &
#Polybar
#sh "$HOME/.config/polybar/launch.sh"
#Monitor
$HOME/.config/qtile/monitor_2.sh
