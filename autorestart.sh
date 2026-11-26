#!/bin/sh

picom &
#Wallpaper
# feh --bg-fill /home/trinhtung/Pictures/wallpapers/flowers/a_close_up_of_a_white_flower.jpg &
# feh --bg-fill /home/trinhtung/Pictures/wallpapers/mountain/benjamin-voros.jpg &
feh --bg-fill /home/trinhtung/Pictures/wallpapers/minimal/this_i_choose_to_do.png &

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
