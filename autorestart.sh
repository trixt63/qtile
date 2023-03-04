#!/bin/sh

#Input method
ibus restart &
#Wallpaper
# feh --bg-fill /home/xuantung/Pictures/wallpapers/nord-wallpapers/ign-0009.png
feh --bg-fill /home/xuantung/Pictures/wallpapers/moon.png
# feh --bg-tile /home/xuantung/Pictures/wallpapers/wallpapers/Monochrome/mono-x.png
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
$HOME/.config/qtile/monitor.sh
