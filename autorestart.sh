#!/bin/sh

#Input method
ibus restart &

#Wallpaper
feh --bg-fill $HOME/Pictures/wallpapers/moon.png &
# feh --bg-tile /home/xuantung/Pictures/wallpapers/wallpapers/Nord/pattern1-nord-2.png
#Compositor

picom &
#bash $HOME/.config/xkb/xcape.sh &

#Mouse scrolling speed
#killall imwheel &
#imwheel &

#Polybar
#sh "$HOME/.config/polybar/launch.sh"

#Monitor
# $HOME/.config/qtile/monitor_2.sh
#autorandr --change

#X keyboard extension
sleep 1 && xkbcomp /home/xuantung/.config/xkb/Xkeymap $DISPLAY
