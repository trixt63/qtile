#!/bin/sh

#Compositor
picom &

#Wallpaper
feh --bg-fill /home/trinhtung/.config/qtile/assets/wallpapers/saudi-mountains.jpg &

#Mouse scrolling speed
#killall imwheel &
#
#Monitor
# autorandr --change &
#
#X keyboard extension
sleep 1.0 && xkbcomp /home/trinhtung/.config/Xkeymap $DISPLAY &
killall xcape &
xcape -e 'Control_L=Escape;'
#
#polybar
# $HOME/.config/polybar/launch.sh
