#!/bin/bash
# Rofi menu to switch audio output: laptop speaker / AUX jack / Bluetooth / HDMI.

CARD="alsa_card.pci-0000_07_00.6"
PROFILE_SPEAKER="HiFi (Mic1, Mic2, Speaker)"
PROFILE_AUX="HiFi (Headphones, Mic1, Mic2)"

# Point the default sink at $1 and move every playing stream onto it.
use_sink() {
    pactl set-default-sink "$1" || return 1
    pactl list short sink-inputs | cut -f1 | while read -r id; do
        pactl move-sink-input "$id" "$1"
    done
}

# Wait up to ~10s for a sink whose name matches $1 to appear, print its name.
wait_sink() {
    for _ in $(seq 20); do
        s=$(pactl list short sinks | cut -f2 | grep -m1 "$1") && { echo "$s"; return 0; }
        sleep 0.5
    done
    return 1
}

current=$(pactl get-default-sink)
mark() { [[ "$current" == *"$1"* ]] && echo "● " || echo "  "; }

entries=("$(mark Speaker)Laptop speaker" "$(mark Headphones)AUX / headphone jack")

# Paired Bluetooth audio devices.
declare -A bt
while read -r _ mac name; do
    bluetoothctl info "$mac" | grep -q "Icon: audio" || continue
    label="$(mark "bluez_output.${mac//:/_}")Bluetooth: $name"
    bt["$label"]=$mac
    entries+=("$label")
done < <(bluetoothctl devices Paired 2>/dev/null || bluetoothctl devices)

# HDMI/DP outputs that have something plugged in.
declare -A hdmi
while read -r sink; do
    port=${sink%__sink}; port=${port##*__}
    pactl list sinks | awk -v s="Name: $sink" '$0 ~ s {f=1} /^Sink #/ {f=0} f' | grep -q "\[Out\] $port:.*, available)" || continue
    label="$(mark "$sink")$port (monitor)"
    hdmi["$label"]=$sink
    entries+=("$label")
done < <(pactl list short sinks | cut -f2 | grep HDMI)

choice=$(printf '%s\n' "${entries[@]}" | rofi -dmenu -i -p "Audio output") || exit 0
[[ -n "$choice" ]] || exit 0

case "$choice" in
    *"Laptop speaker")
        pactl set-card-profile "$CARD" "$PROFILE_SPEAKER"
        sink=$(wait_sink "07_00.6.*Speaker") ;;
    *"AUX / headphone jack")
        pactl set-card-profile "$CARD" "$PROFILE_AUX"
        sink=$(wait_sink "07_00.6.*Headphones") ;;
    *"Bluetooth: "*)
        mac=${bt["$choice"]}
        bluetoothctl power on >/dev/null
        bluetoothctl info "$mac" | grep -q "Connected: yes" || {
            notify-send -t 3000 "Audio" "Connecting ${choice#*Bluetooth: }…"
            bluetoothctl connect "$mac" >/dev/null
        }
        sink=$(wait_sink "bluez_output.${mac//:/_}") ;;
    *)
        sink=${hdmi["$choice"]} ;;
esac

if [[ -n "$sink" ]] && use_sink "$sink"; then
    notify-send -t 2000 "Audio output" "${choice:2}"
else
    notify-send -u critical "Audio output" "Could not switch to ${choice:2}"
fi
