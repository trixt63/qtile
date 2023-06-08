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
killall xcape && sleep 1 &
xcape -e 'Control_L=Escape;' &
sleep 1 && xkbcomp /home/xuantung/.config/xkb/Xkeymap $DISPLAY
