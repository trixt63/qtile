#!/bin/bash

export DISPLAY=:0
export XAUTHORITY=$HOME/.Xauthority

function connect(){
  xrandr --output eDP --off \
    --output HDMI-A-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal \
    --output DisplayPort-0 --off \
    --output DisplayPort-1 --off

}
  
function disconnect(){
  xrandr --output eDP --primary --mode 1920x1080 --pos 0x0 --rotate normal \
    --output HDMI-A-0 --off \
    --output DisplayPort-0 --off --output DisplayPort-1 --off
}

function both() {
  xrandr --output eDP --mode 1920x1080 --pos 1961x0 --rotate normal --output HDMI-A-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DisplayPort-0 --off --output DisplayPort-1 --off
}
   
function HDMI_connected() {
  /usr/bin/xrandr | grep "HDMI-A-0 connected" &> /dev/null
}

function lid_open() {
  cat /proc/acpi/button/lid/LID/state | grep "open" &> /dev/null
}

if HDMI_connected && ! lid_open
then
  connect
fi

if HDMI_connected && lid_open
then
  both
fi

if ! HDMI_connected && lid_open
then
  disconnect
fi
