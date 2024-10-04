from math import ceil, floor
from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles._decorators import *
from modules.widgets import widget_defaults
from modules.utils import get_firefox_instance
from modules.bar_styles._constants import ICONS_PATH, APPS_ICONS_PATH, UPDATE_INTERVAL

OPAQUE = 'ff'
BARSIZE = 30
PAD = 9
_DECORATOR_PADDING = ceil(BARSIZE/10)
_DECORATOR_SIZE = ceil(BARSIZE*1.1 + 1) * 2

ICONS_PATH_SMALL = '/usr/share/icons/Papirus/16x16@2x/panel/'

class Simple:
    def __init__(self, colors):
        self.colors = colors
        self.highlight_method = 'line'

        widget_defaults.update({
            'background': colors.get('background'),
            'foreground': colors.get('foreground'),
            'fontsize': floor(BARSIZE/2)
        })

        # configs
        tasklist_config = dict(
            font=widget_defaults.get('font'),
            foreground=colors.get('foreground_unfocus'),
            background=colors.get('background'),
            fontsize=widget_defaults.get('fontsize') - 2,
            max_title_width=210,
            border=colors.get('background_focus'),
            highlight_method='border',
            borderwidth=1.5,
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

        # widgets
        screen_widgets: list = [
            widget.Clock(
                # format=" %a, %b %d   %H:%M",
                format="  %H:%M  %b %d",
                # font='Font Awesome 5 Free Solid',
                padding=6,
                foreground=colors.get('foreground'),
            ),
            widget.TaskList(**tasklist_config),
            widget.CurrentLayoutIcon(
                # background=colors.get('background_unfocus'),
                fontsize=widget_defaults.get('fontsize') - 1,
                padding=7
            ),
            widget.GroupBox(
                padding_y=6,
                padding_x=6,
                # background=colors.get('background_unfocus'),
                highlight_method=self.highlight_method,
                rounded=False,
                active=colors.get('foreground_focus'),
                inactive=colors.get('foreground_unfocus'),
                # for the focused screen
                this_current_screen_border=colors.get('background_focus'),
                other_current_screen_border=colors.get('background_alt'),
                highlight_color=[_get_highlight_color(self.colors)],  # background for highlight_method='line'
                # for the other screen
                this_screen_border=colors.get('background_focus_alt'),
                other_screen_border=colors.get('background_alt'),
                disable_drag=True
            ),
            widget.Spacer(),
            widget.Mpris2(
                foreground=colors.get('foreground_unfocus'),
                padding=0,
                fontsize=widget_defaults.get('fontsize') - 1,
                max_chars=35,
                name="spotify",
                playing_text=' {track}',
                paused_text=" Pause",
                # format="{xesam:title} - {xesam:artist}",
                display_metadata=["xesam:title", "xesam:artist"],
                objname="org.mpris.MediaPlayer2.spotify"
            ),
            widget.Volume(
                # fontsize=,
                font="Font Awesome 6 Free Solid",
                padding=PAD,
                emoji=True,
                emoji_list=['🔇', '', '', ''],
                background=colors.get('background_unfocus')[1:],
            ),
            widget.Volume(
                fmt='{}',
                mute_format='Muted',
                padding=2,
                background=colors.get('background_unfocus')[1:],
                foreground=colors.get('foreground')[1:],
            ),

            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=0
            ),

            widget.Systray(
                padding=6,
                background=colors.get('background_unfocus'),
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=int(PAD / 3)
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=int(PAD / 3)
            ),
            # widget.QuickExit(),
        ]

        # screen 1
        screen1 = Screen(
            top=bar.Bar(
                widgets=screen_widgets,
                size=BARSIZE,
                background=colors.get('background') + OPAQUE,
            ),
        )

        screen2 = Screen(
            top=bar.Bar(
                [
                    widget.CurrentLayoutIcon(
                        background=colors.get('background_unfocus'),
                        fontsize=widget_defaults.get('fontsize') - 1,
                        padding=6
                    ),
                    widget.GroupBox(
                        padding_y=6,
                        padding_x=7,
                        background=colors.get('background_unfocus'),
                        highlight_method=self.highlight_method,
                        rounded=False,
                        active=colors.get('foreground_focus'),
                        inactive=colors.get('foreground_unfocus'),
                        # for the focused screen
                        this_current_screen_border=colors.get('background_focus'),
                        other_current_screen_border=colors.get('background_alt'),
                        highlight_color=[_get_highlight_color(self.colors)],  # background for highlight_method='line'
                        # for the other screen
                        this_screen_border=colors.get('background_focus_alt'),
                        other_screen_border=colors.get('background_alt'),
                        disable_drag=True
                    ),
                    lower_left_triangle(foreground=colors.get('background_unfocus')),
                    widget.WindowName(
                        foreground=colors.get('foreground_unfocus'),
                        # padding=12,
                        fontsize=widget_defaults.get('fontsize') - 1,
                        max_chars=50
                    ),
                    widget.Mpris2(
                        foreground=colors.get('foreground_unfocus'),
                        fontsize=widget_defaults.get('fontsize') - 1,
                        padding=0,
                        scroll=True,
                        scroll_clear=True,
                        width=185,
                        name="spotify",
                        playing_text=" {track}",
                        paused_text=" Pause",
                        display_metadata=["xesam:title", "xesam:artist"],
                        objname="org.mpris.MediaPlayer2.spotify"
                    ),
                    widget.Spacer(
                        background=colors.get('background'),
                    ),
                    widget.Clipboard(
                        foreground=colors.get('foreground_unfocus'),
                        max_width=30,
                        timeout=None
                    ),
                    lower_right_triangle(foreground=colors.get('background_unfocus')),
                    widget.Volume(
                        padding=1,
                        # theme_path=icons_path,
                        emoji=True,
                        background=colors.get('background_unfocus')[1:],
                        foreground=colors.get('foreground')[1:],
                    ),
                    widget.Volume(
                        fmt='{}',
                        padding=1,
                        background=colors.get('background_unfocus')[1:],
                        foreground=colors.get('foreground')[1:],
                    ),
                    widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        padding=12
                    ),
                    widget.Clock(
                        format=" %H:%M",
                        # font='Font Awesome 5 Free Solid',
                        padding=PAD,
                        background=colors.get('background_unfocus'),
                        foreground=colors.get('foreground'),
                    ),
                    widget.LaunchBar(
                        progs=[('Power', "/home/xuantung/.config/rofi/bin/menu_powermenu", "Power menu")],
                        default_icon='/usr/share/icons/Papirus/22x22/panel/system-devices-panel.svg',
                        background=colors.get('background_unfocus'),
                        foreground=colors.get('foreground'),
                        padding=int(PAD / 3)
                    ),
                    widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        padding=int(PAD / 3)
                    ),
                ],
                BARSIZE,
                background=colors.get('background'),
            ),
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


def _get_highlight_color(colors):
    """Get the highlight_color (the background color)
    for the GroupBox when highlight_method='line',
    in case the color scheme does not have 'background_focus_2'
    """
    colors_list = [colors.get('background_focus_2'),
                   colors.get('background_unfocus'),
                   colors.get('background_alt')]
    return next(color for color in colors_list if color is not None)
