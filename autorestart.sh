#!/bin/sh

#Input method
ibus restart &
#Wallpaper
feh --bg-fill $HOME/Pictures/wallpapers/tory-miles-render.jpg &
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
bash $HOME/.config/qtile/monitor.sh &