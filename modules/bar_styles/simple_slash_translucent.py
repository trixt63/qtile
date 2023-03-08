from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles.decorators import *

PAD = 9
OPAQUE = '00'
icons_path = '/usr/share/icons/Papirus/24x24/panel/'
BARSIZE = 24


class SimpleSlashTranslucent:
    def __init__(self, colors) -> None:
        self.colors = colors
        self.highlight_method = 'line'

        # Widgets config
        widget_defaults.update({
            'background': colors.get('background_unfocus'),
            'foreground': colors.get('foreground')
        })

        launchbar_config = {
            'progs': [(' \u23fb ', "/home/xuantung/.config/rofi/bin/menu_powermenu", "Power menu")],
            'default_icon': icons_path + 'system-devices-panel.svg',
            # 'text_only': True,
            'background': colors.get('background_focus_alt'),
            'padding': 2,
        }

        # Widgets
        separator = widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        size_percent=60,
                        padding=PAD*2
                    )

        widget_volume = (
                    widget.Volume(
                        # theme_path=icons_path,
                        emoji=True,
                        **widget_defaults
                    ),
                    widget.Volume(
                        fmt='{}',
                        background=colors.get('background_unfocus'),
                        foreground=colors.get('foreground'),
                        padding=3
                    )
        )

        widget_battery = (
            widget.BatteryIcon(
                theme_path=icons_path,
                **widget_defaults
            ),
            widget.Battery(
                # format='{char} {percent:2.0%}',
                format='{percent:2.0%}',
                # charge_char='',
                # discharge_char='',
                # empty_char='',
                # unknown_char='',
                **widget_defaults
            )
        )

        mpris2 = widget.Mpris2(
                    foreground=colors.get('foreground_unfocus'),
                    background=colors.get('background_unfocus') + OPAQUE,
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


        # screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(
                                        background=colors.get('background_unfocus'),
                                        fontsize=widget_defaults.get('fontsize') - 1,
                                        padding=7
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
                            background=colors.get('background') + '00',
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=45
                        ),
                        *mpris2,
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
                            update_interval=5.0,
                            **widget_defaults
                        ),
                        separator,
                        widget.Memory(
                            format='{MemUsed: .2f}{mm}',
                            measure_mem='G',
                            update_interval=5.0,
                            **widget_defaults
                        ),
                        separator,
                        *widget_volume,
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=(PAD-2)*2 - 3
                        ),
                        *widget_battery,
                        separator,
                        widget.Clock(
                            format=" %b %d   %H:%M",
                            **widget_defaults
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+2
                        ),
                        widget.LaunchBar(**launchbar_config)
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
                            background=colors.get('background') + OPAQUE,
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_chars=45
                        ),
                        *mpris2,
                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),
                        widget.Clipboard(
                            foreground=colors.get('foreground_unfocus'),
                            fontsize=widget_defaults.get('fontsize') - 1,
                            max_width=45,
                            timeout=None
                        ),
                        lower_right_triangle(foreground=colors.get('background_unfocus')),
                        *widget_volume,
                        separator,
                        widget.Clock(
                            format=" %H:%M",
                            **widget_defaults,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+2
                        ),
                        widget.LaunchBar(**launchbar_config)
                    ],
                    BARSIZE,
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

