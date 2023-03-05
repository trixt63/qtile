from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles.decorators import *

PAD = 10
OPAQUE = '00'
icons_path = '/usr/share/icons/Papirus/24x24/panel/'


class SimpleSlashTranslucent:
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
                            max_chars=45
                        ),
                        widget.Mpris2(
                            foreground=colors.get('foreground_unfocus'),
                            padding=0,
                            fontsize=widget_defaults.get('fontsize') - 1,
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
                            background=colors.get('background') + OPAQUE,
                        ),
                        widget.Systray(
                            padding=4,
                            background=colors.get('background') + OPAQUE,
                            foreground=colors.get('background') + OPAQUE
                        ),
                        lower_right_triangle(foreground=colors.get('background_unfocus'),
                                             background=colors.get('background') + OPAQUE),
                        widget.CPU(
                            format=' {load_percent}%',
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background_unfocus')[1:],
                            padding=0,
                            update_interval=5.0,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+1
                        ),
                        widget.Memory(
                            format='{MemUsed: .2f}{mm}',
                            measure_mem='G',
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background_unfocus')[1:],
                            padding=PAD,
                            update_interval=5.0,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD
                        ),
                        widget.Volume(
                            padding=1,
                            # theme_path=icons_path,
                            emoji=True,
                            background=colors.get('background_unfocus')[1:],
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
                            padding=(PAD-1)*2
                        ),
                        widget.BatteryIcon(
                            theme_path=icons_path,
                            padding=0,
                            background=colors.get('background_unfocus'),
                            foreground=colors.get('foreground')
                        ),
                        widget.Battery(
                            # format='{char} {percent:2.0%}',
                            format='{percent:2.0%}',
                            padding=0,
                            # charge_char='',
                            # discharge_char='',
                            # empty_char='',
                            # unknown_char='',
                            background=colors.get('background_unfocus'),
                            foreground=colors.get('foreground')
                            # foreground=colors.cyan
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD
                        ),
                        widget.Clock(
                            format=" %b %d   %H:%M",
                            # font='Font Awesome 5 Free Solid',
                            padding=PAD,
                            background=colors.get('background_unfocus'),
                            foreground=colors.get('foreground'),
                        ),
                    ],
                    21,
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
                            foreground=colors.get('foreground'),
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=60
                        ),
                        widget.Mpris2(
                            foreground=colors.get('foreground'),
                            padding=0,
                            fontsize=widget_defaults.get('fontsize') - 1,
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
                            background=colors.get('background') + OPAQUE,
                        ),
                        widget.Clipboard(
                            foreground=colors.get('foreground'),
                            max_width=45,
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
                            padding=12,
                            background=colors.get('background_unfocus'),
                            foreground=colors.get('foreground'),
                        ),
                    ],
                    21,
                    background=colors.get('background') + OPAQUE,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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
