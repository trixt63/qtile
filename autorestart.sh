#!/bin/sh

#Input method
ibus restart &
#Wallpaper
feh --bg-fill /home/xuantung/Pictures/wallpapers/moon.png
# feh --bg-tile /home/xuantung/Pictures/wallpapers/wallpapers/Nord/pattern1-nord-2.png
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
# $HOME/.config/qtile/monitor_2.sh
# autorandr --change
