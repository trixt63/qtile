#!/bin/sh

#Wallpaper
feh --bg-fill $HOME/Pictures/wallpapers/moon.png &
# feh --bg-fill /home/xuantung/Pictures/wallpapers/walls/forest-hills.jpg &

#Compositor
picom &

#Mouse scrolling speed
#killall imwheel &
#imwheel &

#Polybar
#sh "$HOME/.config/polybar/launch.sh"

#Monitor
autorandr --change &

#X keyboard extension
sleep 1 && xkbcomp /home/xuantung/.config/xkb/Xkeymap $DISPLAY &
killall xcape && sleep 3 &
xcape -e 'Control_L=Escape;'
