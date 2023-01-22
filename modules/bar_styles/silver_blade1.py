import os

from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen

from modules.bar_styles.decorators import *


class SilverBlades1:
    """An array silver blades on the right corner."""
    def __init__(self, colors) -> None:
        self.colors = colors
        # screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayout(
                            background=colors.white,
                            foreground=colors.black,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            padding=6
                        ),
                        lower_left_triangle(foreground=colors.white, background=colors.black3),
                        widget.GroupBox(
                            padding_y=6,
                            padding_x=7,
                            background=colors.background_unfocus,
                            highlight_method='block',
                            rounded=False,
                            active=colors.foreground_focus,
                            inactive=colors.white4,
                            this_current_screen_border=colors.background_focus,
                            this_current_screen=colors.background_unfocus,
                            disable_drag=True
                        ),
                        lower_left_triangle(foreground=colors.background_unfocus),
                        widget.WindowName(
                            foreground=colors.white2,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=60
                        ),
                        widget.Mpris2(
                            foreground=colors.white2,
                            name="spotify",
                            paused_text=" Pause",
                            playing_text=" {track}",
                            scroll_chars=45,
                            display_metadata=["xesam:title", "xesam:artist"],
                            objname="org.mpris.MediaPlayer2.spotify"
                        ),
                        lower_right_triangle(foreground=colors.white2),
                        widget.CPU(
                            format=' {load_percent}%',
                            foreground=colors.black[1:],
                            background=colors.white2[1:],
                            padding=0,
                            update_interval=5.0,
                        ),
                        lower_right_triangle(foreground=colors.white, background=colors.white2),
                        widget.Memory(
                            format='{MemUsed: .2f}{mm}',
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
                            padding=0,
                            background=colors.white2,
                            foreground=colors.black,
                        ),
                        lower_right_triangle(foreground=colors.white3, background=colors.white2),
                        widget.Systray(
                            padding=4,
                            background=colors.white3
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.white3,
                            padding=4
                        )
                        # widget.QuickExit(),
                    ],
                    18,
                    background=colors.background,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            )
        
        screen2 = Screen(
                bottom=bar.Bar(
                    [
                        widget.CurrentLayout(
                            background=colors.white,
                            foreground=colors.black,
                            fontsize=widget_defaults.get('fontsize') - 1,
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
                            this_current_screen=colors.background_unfocus,
                            disable_drag=True
                        ),
                        lower_left_triangle(foreground=colors.black3),
                        widget.WindowName(
                            foreground=colors.white2,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=60
                        ),
                        widget.Mpris2(
                            foreground=colors.white2,
                            name="spotify",
                            stop_pause_text="Paused", scroll_chars=45,
                            display_metadata=["xesam:title", "xesam:artist"],
                            objname="org.mpris.MediaPlayer2.spotify"
                        ),
                        # lower_right_triangle(foreground=colors.white2),
                        # widget.CPU(
                        #     format=' {load_percent}%',
                        #     foreground=colors.black[1:],
                        #     background=colors.white2[1:],
                        #     padding=0,
                        #     update_interval=5.0,
                        # ),
                        # lower_right_triangle(foreground=colors.white, background=colors.white2),
                        # widget.Memory(
                        #     format='{MemUsed: .2f}{mm}',
                        #     measure_mem='G',
                        #     foreground=colors.black[1:],
                        #     background=colors.white[1:],
                        #     padding=0,
                        #     update_interval=5.0,
                        # ),
                        # lower_right_triangle(foreground=colors.white2, background=colors.white),
                        # widget.Volume(
                        #     padding=2,
                        #     theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                        #     background=colors.white2[1:],
                        #     foreground=colors.black[1:],
                        # ),
                        # widget.Volume(
                        #     fmt='{}',
                        #     font='Font Awesome 5 Free Solid',
                        #     # padding=0,
                        #     background=colors.white2[1:],
                        #     foreground=colors.black[1:],
                        # ),
                        # lower_right_triangle(foreground=colors.white, background=colors.white2),
                        # widget.BatteryIcon(
                        #     theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                        #     padding=1,
                        #     background=colors.white,
                        #     foreground=colors.black
                        # ),
                        # widget.Battery(
                        #     # format='{char} {percent:2.0%}',
                        #     format='{percent:2.0%}',
                        #     font='Font Awesome 5 Free Solid',
                        #     # charge_char='',
                        #     # discharge_char='',
                        #     # empty_char='',
                        #     # unknown_char='',
                        #     background=colors.white,
                        #     foreground=colors.black
                        # ),
                        # lower_right_triangle(foreground=colors.white2, background=colors.white),
                        # widget.Clock(
                        #     # format="%Y-%m-%d %a %I:%M %p",
                        #     format=" %a, %b %d   %I:%M %p",
                        #     font='Font Awesome 5 Free Solid',
                        #     padding=0,
                        #     background=colors.white2,
                        #     foreground=colors.black,
                        # )
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

