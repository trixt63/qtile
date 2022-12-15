import os

from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen

from modules.bar_styles.decorators import *


class SimpleSlash:
    def __init__(self, colors) -> None:
        self.colors = colors
        # widgets
        self._group_box = widget.GroupBox(
                            padding_y=6,
                            padding_x=8,
                            background=colors.background_alt,
                            highlight_method='block',
                            rounded=False,
                            active=colors.foreground_focus,
                            inactive=colors.foreground_alt,
                            this_current_screen_border=colors.background_focus,
                            other_screen_border=colors.white4,
                            disable_drag=True
                        )
        # screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(
                            background=colors.black4,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            padding=6
                        ),
                        self._group_box,
                        lower_left_triangle(foreground=colors.background_alt),
                        widget.WindowName(
                            foreground=colors.foreground_alt,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=50
                        ),

                        widget.Mpris2(
                            foreground=colors.foreground_alt,
                            padding=0,
                            max_chars=35,
                            name="spotify",
                            paused_text=" Pause",
                            playing_text=" {track}",
                            display_metadata=["xesam:title", "xesam:artist"],
                            objname="org.mpris.MediaPlayer2.spotify"
                        ),
                        lower_right_triangle(foreground=colors.background_alt),
                        widget.CPU(
                            format=' {load_percent}%',
                            foreground=colors.foreground[1:],
                            background=colors.background_alt[1:],
                            padding=12,
                            update_interval=5.0,
                        ),
                        widget.Memory(
                            format='{MemUsed: .2f}{mm}',
                            measure_mem='G',
                            foreground=colors.foreground[1:],
                            background=colors.background_alt[1:],
                            padding=12,
                            update_interval=5.0,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_alt,
                            padding=12
                        ),
                        widget.Volume(
                            padding=0,
                            theme_path='/usr/share/icons/Papirus/24x24/panel/',
                            background=colors.background_alt[1:],
                            foreground=colors.cyan[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            padding=0,
                            background=colors.background_alt[1:],
                            foreground=colors.foreground[1:],
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_alt,
                            padding=24
                        ),
                        widget.BatteryIcon(
                            theme_path='/usr/share/icons/Papirus/24x24/panel/',
                            padding=0,
                            background=colors.black4,
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
                            background=colors.background_alt,
                            foreground=colors.foreground
                            # foreground=colors.cyan
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_alt,
                            padding=14
                        ),
                        widget.Clock(
                            # format="%Y-%m-%d %a %I:%M %p",
                            format=" %a, %b %d   %H:%M",
                            # font='Font Awesome 5 Free Solid',
                            padding=12,
                            background=colors.background_alt,
                            foreground=colors.foreground,
                        ),
                        # widget.Sep(
                        #     linewidth=0,
                        #     background=colors.background_alt,
                        #     padding=9
                        # ),
                        # lower_right_triangle(foreground=colors.black4, background=colors.background_alt),
                        widget.Systray(
                            padding=8,
                            background=colors.background_alt
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.background_alt,
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
                            background=colors.background_alt,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            padding=6
                        ),
                        self._group_box,
                        lower_left_triangle(foreground=colors.background_alt),
                        widget.WindowName(
                            foreground=colors.white2,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=60
                        ),

                        widget.Clipboard(
                            foreground=colors.white2,
                            timeout=120
                        ),
                        lower_right_triangle(foreground=colors.background_alt),
                        widget.Volume(
                            padding=0,
                            theme_path='/usr/share/icons/Papirus/24x24/panel/',
                            background=colors.black4[1:],
                            foreground=colors.foreground[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            padding=1,
                            background=colors.black4[1:],
                            foreground=colors.foreground[1:],
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.black4,
                            padding=12
                        ),
                        widget.Clock(
                            # format="%Y-%m-%d %a %I:%M %p",
                            format=" %H:%M",
                            # font='Font Awesome 5 Free Solid',
                            padding=12,
                            background=colors.black4,
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

