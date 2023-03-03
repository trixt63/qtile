from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles.decorators import *

PAD = 10
OPAQUE = 'ff'
UPDATE_INTERVAL = 5.0
BARSIZE = 23
icons_path = '/usr/share/icons/Papirus/24x24/panel/'


class SimpleSlash:
    def __init__(self, colors) -> None:
        self.colors = colors
        # widgets
        self._current_layout_icon = widget.CurrentLayoutIcon(
                                background=colors.get('background_unfocus'),
                                fontsize=widget_defaults.get('fontsize') - 1,
                                padding=7
                             )
        self.highlight_method = 'line'
        # screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        self._current_layout_icon,
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
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=50
                        ),
                        widget.Mpris2(
                            foreground=colors.get('foreground_unfocus'),
                            padding=0,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=35,
                            name="spotify",
                            playing_text=' {track}',
                            paused_text=" Pause",
                            # format="{xesam:title} - {xesam:artist}",
                            display_metadata=["xesam:title", "xesam:artist"],
                            objname="org.mpris.MediaPlayer2.spotify"
                        ),
                        lower_right_triangle(foreground=colors.get('background_unfocus')),
                        # widget.ThermalSensor(
                        #     format=' {temp:.0f}{unit}',
                        #     foreground=colors.get('foreground')[1:],
                        #     background=colors.get('background_unfocus')[1:],
                        #     update_interval=UPDATE_INTERVAL,
                        #     padding=PAD
                        # ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+1
                        ),
                        widget.CPU(
                            format=' {load_percent}%',
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background_unfocus')[1:],
                            padding=0,
                            update_interval=UPDATE_INTERVAL,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+1
                        ),
                        widget.Memory(
                            format=' {MemUsed:.2f}{mm}',
                            measure_mem='G',
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background_unfocus')[1:],
                            padding=PAD,
                            update_interval=UPDATE_INTERVAL,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD-2
                        ),
                        widget.Volume(
                            padding=2,
                            # theme_path=icons_path,
                            emoji=True,
                            background=colors.get('background_unfocus')[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            padding=0,
                            background=colors.get('background_unfocus')[1:],
                            foreground=colors.get('foreground')[1:],
                        ),
                        # widget.Sep(
                        #     linewidth=0,
                        #     background=colors.get('background_unfocus'),
                        #     padding=(PAD-1)*2
                        # ),
                        # widget.BatteryIcon(
                        #     theme_path=icons_path,
                        #     padding=0,
                        #     background=colors.get('background_unfocus'),
                        #     foreground=colors.get('foreground')
                        # ),
                        # widget.Battery(
                        #     format='{percent:2.0%}',
                        #     padding=0,
                        #     # format='{char} {percent:2.0%}',
                        #     # charge_char='',
                        #     # discharge_char='',
                        #     # empty_char='',
                        #     # unknown_char='',
                        #     background=colors.get('background_unfocus'),
                        #     foreground=colors.get('foreground')
                        # ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD
                        ),
                        widget.Clock(
                            # format=" %a, %b %d   %H:%M",
                            format=" %b %d   %H:%M",
                            # font='Font Awesome 5 Free Solid',
                            padding=PAD,
                            background=colors.get('background_unfocus'),
                            foreground=colors.get('foreground'),
                        ),
                        widget.Systray(
                            padding=6,
                            background=colors.get('background_unfocus'),
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=int(PAD/3)
                        )
                        # widget.QuickExit(),
                    ],
                    BARSIZE,
                    background=colors.get('background') + OPAQUE,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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
                            padding=0,
                            scroll=True,
                            scroll_clear=True,
                            width=185,
                            name="spotify",
                            playing_text=" {track}",
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
                            padding=0,
                            theme_path=icons_path,
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
                            padding=12,
                            background=colors.get('background_unfocus'),
                            foreground=colors.get('foreground'),
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


def _get_highlight_color(colors):
    """Get the highlight_color (the background color) 
    for the GroupBox when highlight_method='line',
    in case the color scheme does not have 'background_focus_2'
    """
    colors_list = [colors.get('background_focus_2'),
                   colors.get('background_unfocus'),
                   colors.get('background_alt')]
    return next(color for color in colors_list if color is not None)
