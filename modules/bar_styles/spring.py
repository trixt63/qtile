from math import ceil, floor
from libqtile import bar
from libqtile.config import Screen
from libqtile import widget as widget_og  # for mpris widget

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule, ScreenRule

from modules.widgets import widget_defaults
from modules.bar_styles._constants import ICONS_PATH, APPS_ICONS_PATH, UPDATE_INTERVAL

OPAQUE = 'ff'
BARSIZE = 29
PAD = 10
_DECORATOR_PADDING = ceil(BARSIZE/10)
_DECORATOR_SIZE = ceil(BARSIZE*1.1 + 1) * 2

# Labels for GroupBox2
_originals = ["◉", "◎", "○"]

_nf_circles = ["󰪥",  # \uf0aa4 nf-md-circle_slice_8
               "󰺕",  # \uf0e95 nf-md-circle_double
               "󰄰"]  # \uf0130 nf-md-checkbox_blank_circle_outline

_nf_circles2 = ["",  # \uf192 nf-fa-circle_dot
                ""]  # \uf4aa nf-oct-circle

_nf_bullseye = ["",  # \uf140 nf-fa-bullseye
                "",  # \uf192 nf-fa-circle_dot
                ""]  # \uf4aa nf-oct-circle

_nf_disco = ["",  # \uf140 nf-fa-bullseye
             "",  # \uf192 nf-fa-circle_dot
             ""]  # \uf4aa nf-oct-circle

_LABELS = _nf_circles


class Spring:
    """Simple bar using qtile-extras' GroupBox2, with labels being circles.
    Inspired by u/-basilios-'s Spring dwm rice"""
    def __init__(self, colors):
        self.colors = colors
        self.highlight_method = 'block'

        ###############
        ### WIDGETS ###
        ###############

        _current_layout_config = dict(
            background=colors.get('background'),
            scale=0.8,
            padding=PAD
        )

        _groupbox2_config = dict(
            # font="Hack Nerd Font",
            # font="FiraCode Nerd Font",
            # font="Iosevka Nerd Font",
            fontsize=19,
            # fontsize=18,
            padding_x=10,
            padding_y=0,
            rules=[
                GroupBoxRule(text=_LABELS[0]).when(screen=ScreenRule.THIS),
                GroupBoxRule(text=_LABELS[-2]).when(occupied=True),
                GroupBoxRule(text=_LABELS[-1]).when(),
                GroupBoxRule(text_colour=colors['background_focus']).when(focused=True),
                GroupBoxRule(text_colour=colors['foreground']).when(screen=ScreenRule.NONE),
                GroupBoxRule(text_colour=colors['background_focus_noncurrent']).when(urgent=False),  # not focused, screen not None
                GroupBoxRule(text_colour=colors['urgent']).when(),
            ]
        )

        _tasklist_config = dict(
            foreground=colors.get('foreground_unfocus'),
            background=colors.get('background') + OPAQUE,
            font=widget_defaults.get('font'),
            fontsize=widget_defaults.get('fontsize') - 2,
            icon_size=widget_defaults.get('fontsize') - 1,
            max_title_width=180,
            highlight_method='border',
            border=colors.get('border_focus'),
            borderwidth=1.2,
            theme_mode='preferred',
            theme_path=APPS_ICONS_PATH,
            # spacing=5,
            padding_x=4,
            padding_y=4,
            parse_text=_parse_text,
            markup_focused='<span font_weight="600">{}</span>',
            markup_minimized='<span font_style="italic">_{}</span>',
            markup_maximized='<span>[] {}</span>'
        )

        clock = widget.Clock(
            foreground=colors.get('foreground'),
            format=" %a %b %d  %H:%M",
            padding=PAD*2
        )

        cpu = widget.CPU(
            # foreground=colors.get('foreground'),
            foreground=colors.get('orange'),
            format=' {load_percent}%',
            update_interval=UPDATE_INTERVAL,
            padding=PAD/2,
        )

        memory = widget.Memory(
            foreground=colors.get('green'),
            format='󰘚 {MemUsed:.2f}{mm}',
            measure_mem='G',
            update_interval=UPDATE_INTERVAL,
            padding=PAD/2,
        )

        thermal = widget.ThermalSensor(
                            format=' {temp:.0f}{unit}',
                            tag_sensor="CPU",
                            padding=PAD/2,
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background')[1:],
                            update_interval=UPDATE_INTERVAL)

        volume_widgets = (
                    widget.Volume(
                        font="Font Awesome 6 Free Solid",
                        foreground=colors.get('foreground'),
                        background=colors.get('background'),
                        padding=PAD/2,
                        emoji=True,
                        emoji_list=['', '', '', ''],
                    ),
                    widget.Volume(
                        fmt='{}',
                        foreground=colors.get('foreground'),
                        background=colors.get('background'),
                        padding=1
                    )
        )

        battery_widgets = (
            widget.Sep(linewidth=0, padding=PAD-4),
            widget.BatteryIcon(
                foreground=colors.get('foreground'),
                theme_path=ICONS_PATH,
                padding=-2,
            ),
            widget.Battery(
                foreground=colors.get('foreground'),
                format='{percent:2.0%}',
                padding=0
            ),
            widget.Sep(linewidth=0, padding=PAD-2),
        )

        net = widget.Net(
            foreground=colors.get('foreground')[1:],
            background=colors.get('background')[1:],
            padding=PAD*2,
            format='󰓅 {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
            update_interval=UPDATE_INTERVAL
        )

        mpris2_spotify = widget_og.Mpris2(
            background=colors.get('background') + OPAQUE,
            foreground=colors.get('foreground_unfocus'),
            padding=PAD,
            font=widget_defaults.get('font'),
            fontsize=widget_defaults.get('fontsize') - 1,
            scroll=True,
            scroll_clear=False,
            scroll_delay=0.5,
            width=180,
            name="spotify",
            playing_text=" {track}",
            paused_text=" Spotify",
            no_metadata_text=" Spotify playing",
            display_metadata=['xesam:title', 'xesam:artist'],
            objname="org.mpris.MediaPlayer2.spotify")

        systray = widget.Systray(padding=6,
                                 background=colors.get('background'))

        sep = widget.Sep(
            linewidth=0,
            background=colors.get('background'),
            padding=PAD)

        spacer = widget.Spacer()

        widgets_list_1 = [
                widget.CurrentLayoutIcon(**_current_layout_config),
                widget.GroupBox2(**_groupbox2_config),
                sep, widget.TaskList(**_tasklist_config),
                clock,
                spacer,
                mpris2_spotify,
                sep, *volume_widgets, sep, *battery_widgets, systray, sep
        ]

        widgets_list_2 = [
                widget.CurrentLayoutIcon(**_current_layout_config),
                widget.GroupBox2(**_groupbox2_config),
                sep, widget.TaskList(**_tasklist_config),
                clock,
                spacer,
                mpris2_spotify,
                sep, *volume_widgets, sep, *battery_widgets, sep, thermal, sep, cpu, sep, memory, sep
            ]

        ###############
        ### SCREENS ###
        ###############

        screen1 = Screen(
            top=bar.Bar(
                widgets=widgets_list_1,
                size=BARSIZE,
                background=colors.get('background') + OPAQUE,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
        )

        screen2 = Screen(
            top=bar.Bar(
                widgets=widgets_list_2,
                size=BARSIZE,
                background=colors.get('background') + OPAQUE,
            )
        )

        self.screens = [
            screen1,
            screen2
        ]


def _parse_text(text):
    """remove redundant texts in some window names"""
    for string in ["MongoDB Compass - "]:
        if text.startswith(string):
            text = text.replace(string, "")
            text = text + string[-3:] + string[:-3]
        return text

