from math import ceil, floor
from libqtile import bar
from libqtile.config import Screen

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.layout.decorations import ConditionalBorder, GradientBorder, GradientFrame, RoundedCorners
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBox2, GroupBoxRule, ScreenRule


from modules.widgets import widget_defaults
from modules.utils import get_firefox_instance
from modules.bar_styles._constants import ICONS_PATH, APPS_ICONS_PATH, UPDATE_INTERVAL
from modules.bar_styles._decorators import lower_left_triangle, lower_right_triangle


OPAQUE = 'ff'
BARSIZE = 33
PAD = 10
_DECORATOR_PADDING = ceil(BARSIZE/10)
_DECORATOR_SIZE = ceil(BARSIZE*1.1 + 1) * 2


def set_label(rule, box):
    if box.focused:
        rule.text = "◉"
    elif box.occupied:
        rule.text = "◎"
    else:
        rule.text = "○"

    return True


GroupBoxRule().when(func=set_label)


class Simple:
    def __init__(self, colors):
        self.colors = colors
        self.highlight_method = 'block'

        # widgets
        current_layout_icon = widget.CurrentLayoutIcon(
            background=colors.get('background_unfocus'),
            fontsize=widget_defaults.get('fontsize') - 1,
            padding=7
        )

        _groupbox2_config = dict(
            fontsize=20,
            padding_x=6,
            rules=[
                  GroupBoxRule(text=''),
                  GroupBoxRule(text_colour=colors['background_focus']).when(screen=ScreenRule.THIS),
                  GroupBoxRule(text_colour=colors['background_focus_alt']).when(screen=ScreenRule.OTHER),
                  GroupBoxRule(text_colour=colors['foreground']).when(occupied=True),
                  GroupBoxRule(text_colour=colors['background_alt']).when(occupied=False),
                  GroupBoxRule(text_colour=colors['urgent']).when(urgent=False)
            ]
        )
        groupbox2_2 = widget.GroupBox2(**_groupbox2_config)

        _tasklist_config = dict(
            font=widget_defaults.get('font'),
            foreground=colors.get('background'),
            # foreground=colors.get('foreground_unfocus'),
            background=colors.get('background') + OPAQUE,
            fontsize=widget_defaults.get('fontsize') - 2,
            max_title_width=210,
            border=colors.get('background_focus'),
            highlight_method='block',
            # border=colors.get('foreground'),
            # highlight_method='border',
            # borderwidth=1.5,
            icon_size=widget_defaults.get('fontsize') - 1,
            theme_mode='preferred',
            theme_path=APPS_ICONS_PATH,
            margin=3,
            padding=3,
            parse_text=_parse_text,
            markup_focused='<span font_weight="600">{}</span>',
            markup_minimized='<span font_style="italic">_{}</span>',
            markup_maximized='<span>[] {}</span>'
        )

        clock = widget.Clock(
            format=" %a %b %d  %H:%M",
            # fontsize=widget_defaults.get('fontsize') - 1
        )

        cpu = widget.CPU(
            foreground=colors.get('foreground'),
            format=' {load_percent}%',
            update_interval=UPDATE_INTERVAL,
            padding=PAD/2,
            **widget_defaults
        )

        memory = widget.Memory(
            foreground=colors.get('foreground'),
            format='󰘚 {MemUsed:.2f}{mm}',
            measure_mem='G',
            update_interval=UPDATE_INTERVAL,
            padding=PAD/2,
            **widget_defaults
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
                        padding=PAD/2-1,
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
            widget.BatteryIcon(
                theme_path=ICONS_PATH,
                padding=-2,
            ),
            widget.Battery(
                format='{percent:2.0%}',
                padding=0
            )
        )

        net = widget.Net(
            foreground=colors.get('foreground')[1:],
            background=colors.get('background')[1:],
            padding=PAD*2,
            format='󰓅 {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
            update_interval=UPDATE_INTERVAL
        )

        _mpris2_spotify_config = dict(background=colors.get('background'),
                                      foreground=colors.get('foreground_unfocus'),
                                      # fontshadow=colors.get('green'),
                                      padding=PAD,
                                      font=widget_defaults.get('font'),
                                      fontsize=widget_defaults.get('fontsize') - 1,
                                      scroll=True,
                                      scroll_clear=True,
                                      scroll_delay=0.5,
                                      width=170,
                                      name="spotify",
                                      playing_text=" {track}",
                                      paused_text=" Spotify",
                                      no_metadata_text=" Spotify playing",
                                      display_metadata=['xesam:title', 'xesam:artist'],
                                      # poll_interval=1,
                                      objname="org.mpris.MediaPlayer2.spotify")

        mpris2_spotify = widget.Mpris2(**_mpris2_spotify_config)

        systray = widget.Systray(padding=6,
                                 background=colors.get('background'))

        sep = widget.Sep(
            linewidth=0,
            background=colors.get('background'),
            padding=PAD)

        spacer = widget.Spacer()

        widgets_list_1 = [
                current_layout_icon, widget.GroupBox2(**_groupbox2_config), sep, widget.TaskList(**_tasklist_config),
                clock, spacer,
                mpris2_spotify, sep, *volume_widgets, sep, *battery_widgets, sep, systray, sep
        ]

        widgets_list_2 = [
                current_layout_icon, widget.GroupBox2(**_groupbox2_config), sep, widget.TaskList(**_tasklist_config),
                clock, spacer,
                widget.Mpris2(**_mpris2_spotify_config),
                sep, thermal, sep, cpu, sep, memory, sep, *volume_widgets, sep, *battery_widgets, sep
            ]

        # screen 1
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


def rectdeco(hexcolor):
    return RectDecoration(
        filled=True,
        colour=hexcolor,
        padding_y= 5,
        padding_x= 0,
        radius=4
    )


def _parse_text(text):
    """remove redundant texts in some window names"""
    for string in ["MongoDB Compass - "]:
        if text.startswith(string):
            text = text.replace(string, "")
            text = text + string[-3:] + string[:-3]
        return text


def _get_highlight_color(colors):
    """Get the highlight_color (the background color)
    for the GroupBox when highlight_method='line',
    in case the color scheme does not have 'background_focus_2'
    """
    colors_list = [colors.get('background_focus_2'),
                   colors.get('background_unfocus'),
                   colors.get('background_alt')]
    return next(color for color in colors_list if color is not None)
