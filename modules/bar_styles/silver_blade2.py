import os

from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles._decorators import *


class SilverBlades2:
    """An array silver blades on the right corner - Top bar version.
    The middle of the bar is transparent. The Systray is also moved to
    the right of the middle part"""
    def __init__(self, colors) -> None:
        self.colors = colors
        # screen 1:
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
                        foreground=colors.light1,
                        # padding=12,
                        fontsize=widget_defaults.get('fontsize') - 1,
                        max_chars=60
                    ),
                    widget.Systray(
                        padding=5,
                        icon_size=18
                    ),

                    lower_right_triangle(foreground=colors.light1),
                    widget.CPU(
                        format=' {load_percent}%',
                        foreground=colors.black[1:],
                        background=colors.light1[1:],
                        padding=0,
                        update_interval=5.0,
                    ),
                    lower_right_triangle(foreground=colors.white, background=colors.light1),
                    widget.Memory(
                        format='{MemUsed: .2f}{mm}',
                        measure_mem='G',
                        foreground=colors.black[1:],
                        background=colors.white[1:],
                        padding=0,
                        update_interval=5.0,
                    ),
                    lower_right_triangle(foreground=colors.light1, background=colors.white),
                    widget.Volume(
                        padding=2,
                        theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                        background=colors.light1[1:],
                        foreground=colors.black[1:],
                    ),
                    widget.Volume(
                        fmt='{}',
                        font='Font Awesome 5 Free Solid',
                        # padding=0,
                        background=colors.light1[1:],
                        foreground=colors.black[1:],
                    ),
                    lower_right_triangle(foreground=colors.white, background=colors.light1),
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
                    lower_right_triangle(foreground=colors.light1, background=colors.white),
                    widget.Clock(
                        # format="%Y-%m-%d %a %I:%M %p",
                        format=" %a, %b %d   %I:%M %p",
                        font='Font Awesome 5 Free Solid',
                        background=colors.light1,
                        foreground=colors.black
                    ),
                    widget.Sep(
                        linewidth=0,
                        background=colors.light1,
                        padding=10
                    )
                    # widget.QuickExit(),
                ],
                19,
                background=colors.background+'00',
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
        )
        # screen 2
        screen2 = Screen(
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
                            foreground=colors.light1,
                            # padding=12,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=60
                        ),
                        widget.Mpris2(
                            foreground=colors.light1,
                            name="spotify",
                            paused_text=" Pause",
                            playing_text=" {track}",
                            scroll_chars=45,
                            display_metadata=["xesam:title", "xesam:artist"],
                            objname="org.mpris.MediaPlayer2.spotify"
                        ),
                        # lower_right_triangle(foreground=colors.white2),
                        # widget.CPU(
                        #     format='  {load_percent}%',
                        #     foreground=colors.black[1:],
                        #     background=colors.white2[1:],
                        #     padding=0,
                        #     update_interval=5.0,
                        # ),
                        # lower_right_triangle(foreground=colors.white, background=colors.white2),
                        # widget.Memory(
                        #     format=' {MemUsed: .2f}{mm}',
                        #     measure_mem='G',
                        #     foreground=colors.black[1:],
                        #     background=colors.white[1:],
                        #     padding=0,
                        #     update_interval=5.0,
                        # ),
                        lower_right_triangle(foreground=colors.light1),
                        widget.Volume(
                            padding=2,
                            theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                            background=colors.light1[1:],
                            foreground=colors.black[1:],
                        ),
                        widget.Volume(
                            fmt='{}',
                            font='Font Awesome 5 Free Solid',
                            # padding=0,
                            background=colors.light1[1:],
                            foreground=colors.black[1:],
                        ),
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
                        lower_right_triangle(foreground=colors.white, background=colors.light1),
                        widget.Clock(
                            # format="%Y-%m-%d %a %I:%M %p",
                            format="  %I:%M %p",
                            font='Font Awesome 5 Free Solid',
                            background=colors.white,
                            foreground=colors.black
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.white,
                            padding=10
                        )
                    ],
                    19,
                    background=colors.background+'00',
                ),
            )

        self.screens = [
            screen1,
            screen2
        ]

