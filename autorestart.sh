#!/bin/sh

#Input method
ibus restart &
#Wallpaper
# feh --bg-fill /home/xuantung/Pictures/wallpapers/nord-wallpapers/ign_unsplash18.png &
feh --bg-fill /home/xuantung/Pictures/wallpapers/nord-wallpapers/nord_lake.png
# feh --bg-fill /home/xuantung/Pictures/wallpapers/nord-wallpapers/debian-galaxy.png
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
bash $HOME/.config/qtile/monitor.sh
