#!/bin/sh

picom &
#Wallpaper
#feh --bg-fill /home/trinhtung/.config/qtile/assets/wallpapers/saudi-mountains.jpg &
#feh --bg-fill /home/trinhtung/Pictures/wallpapers/nature/a_beach_with_waves_and_rocks.jpg &
#feh --bg-fill /home/trinhtung/Pictures/wallpapers/nature/a_small_plant_in_a_pot.jpg &
#feh --bg-fill /home/trinhtung/Pictures/wallpapers/flowers/a_close_up_of_a_white_flower.jpg &
feh --bg-fill /home/trinhtung/Pictures/wallpapers/mountain/benjamin-voros.jpg &
#feh --bg-fill /home/trinhtung/Pictures/wallpapers/anime/a_bird_flying_in_the_sky.png %

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
