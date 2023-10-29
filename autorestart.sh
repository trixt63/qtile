#!/bin/sh
#Wallpaper
#feh --bg-fill /home/xuantung/Pictures/wallpapers/moon.png &
feh --bg-fill /home/xuantung/Pictures/wallpapers/walls/saudi-mountains.jpg


#Compositor
picom &

#Mouse scrolling speed
#killall imwheel &

#Monitor
autorandr --change &

#X keyboard extension
sleep 1 && xkbcomp /home/xuantung/.config/xkb/Xkeymap $DISPLAY &
killall xcape &
sleep 1 && xcape -e 'Control_L=Escape;'

#polybar
# $HOME/.config/polybar/launch.sh
