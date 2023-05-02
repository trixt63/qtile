#!/bin/sh

#Input method
ibus restart &

#Wallpaper
feh --bg-fill $HOME/Pictures/wallpapers/moon.png &

#Compositor
picom &

#Mouse scrolling speed
#killall imwheel &
#imwheel &

#Polybar
#sh "$HOME/.config/polybar/launch.sh"

#Monitor
# $HOME/.config/qtile/monitor_2.sh
autorandr --change &

#X keyboard extension
sleep 1 && xkbcomp /home/xuantung/.config/xkb/Xkeymap $DISPLAY &
killall xcape && sleep 1 &
xcape -e 'Control_L=Escape;'
