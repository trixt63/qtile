import os

from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen

from modules.bar_styles.decorators import *


class SilverBlades:
    def __init__(self, colors) -> None:
        self.colors = colors
        self.screens = [
            Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayout(
                            background=colors.white,
                            foreground=colors.black,
                            fontsize=13,
                            padding=6
                        ),
                        lower_left_triangle(foreground=colors.white, background=colors.black3),
                        widget.GroupBox(
                            padding_y=6,
                            padding_x=7,
                            background=colors.black3,
                            highlight_method='block',
                            rounded=False,
                            active=colors.foreground_focus,
                            inactive=colors.white4,
                            this_current_screen_border=colors.background_focus,
                            this_current_screen=colors.background_alt,
                            disable_drag=True
                        ),
                        lower_left_triangle(foreground=colors.black3),
                        widget.WindowName(
                            foreground=colors.white2,
                            # padding=12,
                            fontsize=13,
                            max_chars=60
                        ),
                        widget.Systray(
                            padding=6,
                        ),

                        lower_right_triangle(foreground=colors.white2),
                        widget.CPU(
                            format='  {load_percent}%',
                            foreground=colors.black[1:],
                            background=colors.white2[1:],
                            padding=0,
                            update_interval=5.0,
                        ),
                        lower_right_triangle(foreground=colors.white, background=colors.white2),
                        widget.Memory(
                            format=' {MemUsed: .2f}{mm}',
                            measure_mem='G',
                            foreground=colors.black[1:],
                            background=colors.white[1:],
                            padding=0,
                            update_interval=5.0,
                        ),
                        lower_right_triangle(foreground=colors.white2, background=colors.white),
                        widget.Volume(
                            padding=2,
                            theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                            background=colors.white2[1:],
                            foreground=colors.black[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            font='Font Awesome 5 Free Solid',
                            # padding=0,
                            background=colors.white2[1:],
                            foreground=colors.black[1:],
                        ),
                        lower_right_triangle(foreground=colors.white, background=colors.white2),
                        widget.BatteryIcon(
                            theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                            padding=1,
                            background=colors.white,
                            foreground=colors.black
                        ),
                        widget.Battery(
                            # format='{char} {percent:2.0%}',
                            format='{percent:2.0%}',
                            font='Font Awesome 5 Free Solid',
                            # charge_char='',
                            # discharge_char='',
                            # empty_char='',
                            # unknown_char='',
                            background=colors.white,
                            foreground=colors.black
                        ),
                        lower_right_triangle(foreground=colors.white2, background=colors.white),
                        widget.Clock(
                            # format="%Y-%m-%d %a %I:%M %p",
                            format=" %a, %b %d   %I:%M %p",
                            font='Font Awesome 5 Free Solid',
                            background=colors.white2,
                            foreground=colors.black
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.white2,
                            padding=10
                        )
                        # widget.QuickExit(),
                    ],
                    20,
                    background=colors.background+'00',
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            )
        ]

