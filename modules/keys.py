from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal(preference='xfce4-terminal')
sink_name = "@DEFAULT_SINK@"

PATH_LAUNCHER = "/home/trinhtung/.config/rofi/scripts/launcher_t1"
PATH_POWERMENU = "/home/trinhtung/.config/rofi/scripts/powermenu_t2"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key([mod, "control", "shift"], "q", lazy.spawn("qtile cmd-obj -o cmd -f shutdown"), desc="Exit Qtile"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.shrink_main(), desc="Shrink main window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_main(), desc="Grow main window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "k", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset secondary window sizes"),
    Key([mod], "r", lazy.layout.reset(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle next layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle previous layouts"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    # Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "n", lazy.window.toggle_minimize(), desc="Minimize window"),
    Key([mod, "shift"], "m", lazy.window.toggle_maximize(), desc="Maximize window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "r", lazy.restart(), desc="Reload all the config and modules"),
    Key([mod, "mod1", "shift"], "q", lazy.shutdown(), desc="Close Windows"),
    Key([mod, "control"], "x", lazy.spawn("$HOME/.local/bin/betterlockscreen -l --off 120"), desc="Lock screen"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Change screen
    Key([mod], 'period', lazy.prev_screen(), desc='Previous monitor'),
    Key([mod], 'slash', lazy.next_screen(), desc='Next monitor'),
    Key([mod], 'minus', lazy.prev_screen(), desc='Previous monitor'),
    Key([mod], 'equal', lazy.next_screen(), desc='Next monitor'),
    # Rofi
    Key([mod], "d", lazy.spawn(PATH_LAUNCHER), desc="spawn app launcher"),
    Key([mod], "p", lazy.spawn(PATH_POWERMENU), desc="spawn power menu"),
    # Screenshot
    Key(["control", "mod3"], "super_r", lazy.spawn("xfce4-screenshooter -w"), desc="Screenshot a window"),
    Key(["control", "shift"], "super_r", lazy.spawn("xfce4-screenshooter -r"), desc="Screenshot part of the screen"),
    # Clipboard
    # Key(["mod1"], "c", lazy.spawn("xfce4-popup-clipman"), desc="Clipboard pop=up"),
    # Sound
    Key([], "XF86AudioLowerVolume", lazy.spawn(f"pactl set-sink-volume {sink_name} -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f"pactl set-sink-volume {sink_name} +5%")),
    Key([], "XF86AudioMute", lazy.spawn(f"pactl set-sink-mute {sink_name} toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle")),
    # Media
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    # Key([], "XF86Eject", lazy.spawn("")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # Applications
    # Key([mod, "control"], "w", lazy.spawn("firefox"), desc="Web browser"),
    Key([mod], "f", lazy.spawn("thunar"), desc="File manager"), 
    Key([mod, "control"], "v", lazy.spawn("pavucontrol"), desc="Volume & sound manager"),
    Key([mod, "control"], "m", lazy.spawn("xfce4-taskmanager"), desc="Task manager")
]
