#!/bin/sh

#Compositor
picom &

#Wallpaper
feh --bg-fill /home/xuantung/.config/qtile/assets/wallpapers/saudi-mountains.jpg &

#Mouse scrolling speed
#killall imwheel &
#
#Monitor
# autorandr --change &
#
#X keyboard extension
sleep 1.5 && xkbcomp /home/xuantung/.config/xkb/Xkeymap $DISPLAY &
killall xcape &
xcape -e 'Control_L=Escape;'
#
#polybar
# $HOME/.config/polybar/launch.sh
