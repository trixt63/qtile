import os

from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen

from modules.bar_styles.decorators import *


class SimpleSlash:
    def __init__(self, colors) -> None:
        self.colors = colors
        # widgets
        self._current_layout_icon = widget.CurrentLayoutIcon(
                                background=colors.background_unfocus,
                                fontsize=widget_defaults.get('fontsize') - 1,
                                padding=6
                             )
        # screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        self._current_layout_icon,
                        widget.GroupBox(
                            padding_y=6,
                            padding_x=7,
                            background=colors.background_unfocus,
                            highlight_method='block',
                            rounded=False,
                            active=colors.foreground_focus,
                            inactive=colors.foreground_unfocus,
                            this_current_screen_border=colors.background_focus,
                            other_screen_border=colors.background_unfocus,
                            disable_drag=True
                        ),
                        lower_left_triangle(foreground=colors.background_unfocus),
                        widget.WindowName(
                            foreground=colors.foreground_unfocus,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=50
                        ),

                        widget.Mpris2(
                            foreground=colors.foreground_unfocus,
                            padding=0,
                            max_chars=35,
                            name="spotify",
                            paused_text=" Pause",
                            playing_text=" {track}",
                            display_metadata=["xesam:title", "xesam:artist"],
                            objname="org.mpris.MediaPlayer2.spotify"
                        ),
                        lower_right_triangle(foreground=colors.background_unfocus),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=3
                        ),
                        widget.CPU(
                            format=' {load_percent}%',
                            foreground=colors.foreground[1:],
                            background=colors.background_unfocus[1:],
                            padding=0,
                            update_interval=5.0,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=12
                        ),
                        widget.Memory(
                            format='{MemUsed: .2f}{mm}',
                            measure_mem='G',
                            foreground=colors.foreground[1:],
                            background=colors.background_unfocus[1:],
                            padding=12,
                            update_interval=5.0,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=12
                        ),
                        widget.Volume(
                            padding=0,
                            theme_path='/usr/share/icons/Papirus/24x24/panel/',
                            background=colors.background_unfocus[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            padding=0,
                            background=colors.background_unfocus[1:],
                            foreground=colors.foreground[1:],
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=24
                        ),
                        widget.BatteryIcon(
                            theme_path='/usr/share/icons/Papirus/24x24/panel/',
                            padding=0,
                            background=colors.background_unfocus,
                            foreground=colors.foreground
                        ),
                        widget.Battery(
                            # format='{char} {percent:2.0%}',
                            format='{percent:2.0%}',
                            padding=0,
                            # charge_char='',
                            # discharge_char='',
                            # empty_char='',
                            # unknown_char='',
                            background=colors.background_unfocus,
                            foreground=colors.foreground
                            # foreground=colors.cyan
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=14
                        ),
                        widget.Clock(
                            # format="%Y-%m-%d %a %I:%M %p",
                            format=" %a, %b %d   %H:%M",
                            # font='Font Awesome 5 Free Solid',
                            padding=12,
                            background=colors.background_unfocus,
                            foreground=colors.foreground,
                        ),
                        widget.Systray(
                            padding=8,
                            background=colors.background_unfocus
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=6
                        )
                        # widget.QuickExit(),
                    ],
                    21,
                    background=colors.background,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            )
        
        screen2 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(
                            background=colors.background_unfocus,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            padding=6
                        ),
                        widget.GroupBox(
                            padding_y=6,
                            padding_x=7,
                            background=colors.background_unfocus,
                            highlight_method='block',
                            rounded=False,
                            active=colors.foreground_focus,
                            inactive=colors.foreground_unfocus,
                            this_current_screen_border=colors.background_focus,
                            other_screen_border=colors.background_unfocus,
                            disable_drag=True
                        ),
                        lower_left_triangle(foreground=colors.background_unfocus),
                        widget.WindowName(
                            foreground=colors.foreground,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=60
                        ),

                        widget.Clipboard(
                            foreground=colors.foreground,
                            timeout=120
                        ),
                        lower_right_triangle(foreground=colors.background_unfocus),
                        widget.Volume(
                            padding=0,
                            theme_path='/usr/share/icons/Papirus/24x24/panel/',
                            background=colors.background_unfocus[1:],
                            foreground=colors.foreground[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            padding=1,
                            background=colors.background_unfocus[1:],
                            foreground=colors.foreground[1:],
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_unfocus,
                            padding=12
                        ),
                        widget.Clock(
                            # format="%Y-%m-%d %a %I:%M %p",
                            format=" %H:%M",
                            # font='Font Awesome 5 Free Solid',
                            padding=12,
                            background=colors.background_unfocus,
                            foreground=colors.foreground,
                        ),
                    ],
                    21,
                    background=colors.background,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            )
        self.screens = [
            screen1,
            screen2
        ]

