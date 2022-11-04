import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.colors.github_dark import GithubDark
from modules.colors.space_gray import SpaceGray

colors = GithubDark()

def lower_right_triangle(background=None, foreground='#ffffff'):
    return widget.TextBox(
        text='\u25E2',
        fontsize=59,
        padding=0,
        background=background,
        foreground=foreground
    )

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(linewidth=0),
                widget.GroupBox(
                  padding_y=6,
                  padding_x=12,
                  highlight_method='block',
                  rounded=False,
                  active=colors.foreground_focus,
                  inactive=colors.white4,
                  this_current_screen_border=colors.background_focus,
                  this_current_screen=colors.background_alt
                ),
                widget.WindowName(
                    foreground=colors.white2,
                    padding=12,
                ),
                # widget.Spacer(),
                # widget.Prompt(),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.CurrentLayout(
                    background=colors.background,
                ),
                lower_right_triangle(foreground=colors.white),
                widget.CPU(
                    format=' {load_percent}%  ',
                    # format='CPU: {load_percent}%  ',
                    foreground=colors.black[1:],
                    background=colors.white[1:],
                    update_interval=5.0,
                ),
                widget.Memory(
                    format='{MemUsed: .2f}{mm}',
                    # format='MEM: {MemUsed: .2f}{mm}',
                    measure_mem='G',
                    padding=2,
                    foreground=colors.black[1:],
                    background=colors.white[1:],
                    update_interval=5.0,
                ),
                lower_right_triangle(foreground=colors.white2, background=colors.white),
                widget.Volume(
                    # fmt='VOL: {}',
                    padding=2,
                    theme_path='/usr/share/icons/Papirus-Light/24x24/panel/',
                    background=colors.white2[1:],
                    foreground=colors.black[1:],
                ),
                widget.Volume(
                    fmt='{}',
                    font='Font Awesome 5 Free Solid',
                    padding=0,
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
                    format="%Y-%m-%d %a %I:%M %p",
                    font='Font Awesome 5 Free Solid',
                    background=colors.white2,
                    foreground=colors.black
                ),
                lower_right_triangle(foreground=colors.white3, background=colors.white2),
                widget.Systray(
                    background=colors.white3
                ),
                # widget.QuickExit(),
            ],
            25,
            background=colors.background,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
