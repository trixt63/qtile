import os

from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen

from modules.bar_styles.decorators import *


class Simple:
    def __init__(self, colors):
        self.colors = colors
        self.screens = [
            Screen(
                top=bar.Bar(
                    [
                        widget.GroupBox(
                          padding_y=6,
                          padding_x=9,
                          highlight_method='block',
                          rounded=False,
                          active=colors.foreground_focus,
                          inactive=colors.white4,
                          this_current_screen_border=colors.background_focus,
                          this_current_screen=colors.background_unfocus
                        ),
                        widget.WindowName(
                            foreground=colors.white2,
                            padding=12,
                            fontsize=13,
                            max_chars=60
                        ),
                        widget.CurrentLayout(
                            background=colors.background,
                            fontsize=13,
                            padding=10,
                        ),
                        widget.CPU(
                            format=' CPU {load_percent}%',
                            foreground=colors.yellow[1:],
                            padding=10,
                            update_interval=5.0,
                        ),
                        widget.Memory(
                            # format=' {MemUsed: .2f}{mm}',
                            format=' MEM{MemUsed: .2f}{mm}',
                            measure_mem='G',
                            foreground=colors.yellow[1:],
                            padding=10,
                            update_interval=5.0,
                        ),
                        # widget.Volume(
                        #     # fmt='VOL: {}',
                        #     padding=2,
                        #     theme_path='/usr/share/icons/Papirus-Dark/24x24/panel/',
                        #     foreground=colors.green[1:],
                        # ),
                        widget.Volume(
                            fmt=' {}',
                            # font='Font Awesome 5 Free Solid',
                            padding=10,
                            foreground=colors.green[1:],
                        ),
                        # widget.BatteryIcon(
                        #     theme_path='/usr/share/icons/Papirus-Dark/24x24/panel/',
                        #     padding=1,
                        #     foreground=colors.green
                        # ),
                        widget.Battery(
                            format='{char} {percent:2.0%}',
                            # format='{percent:2.0%}',
                            # font='Font Awesome 5 Free Solid',
                            padding=10,
                            charge_char='',
                            discharge_char='',
                            empty_char='',
                            unknown_char='',
                            foreground=colors.green
                        ),
                        widget.Clock(
                            format="%Y-%m-%d %a %I:%M %p",
                            # font='Font Awesome 5 Free Solid',
                            foreground=colors.purple,
                            padding=10,
                        ),
                        widget.WidgetBox(
                            widgets = [
                                widget.Systray(
                                    background=colors.white3,
                                    padding=5,
                                ),
                            ],
                            # close_button_location='right',
                            background=colors.white3,
                            text_closed='  ',
                            text_open='  ',
                            fontsize=17,
                        )
                        # widget.QuickExit(),
                    ],
                    23,
                    background=colors.background,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            )
        ]
