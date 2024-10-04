#!/bin/sh

picom &
#Wallpaper
# feh --bg-fill /home/trinhtung/.config/qtile/assets/wallpapers/saudi-mountains.jpg &
feh --bg-fill /home/trinhtung/Pictures/wallpapers/nature/a_beach_with_waves_and_rocks.jpg &
# feh --bg-fill /home/trinhtung/Pictures/wallpapers/fogsmoke/a_chairlifts_on_a_mountain.jpg &
# feh --bg-fill /home/trinhtung/Pictures/wallpapers/nature/a_small_plant_in_a_pot.jpg &
# feh --bg-fill /home/trinhtung/Pictures/wallpapers/nature/a_foggy_landscape_with_trees_and_grass.jpg &
#feh --bg-fill /home/trinhtung/Pictures/wallpapers/scenery/benjamin-voros.jpg &

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
