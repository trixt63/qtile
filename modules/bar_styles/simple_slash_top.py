from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles._decorators import *
from modules.widgets import widget_defaults


PAD = 9
OPAQUE = '00'
icons_path = '/usr/share/icons/Papirus/24x24/panel/'
BARSIZE = 27
UPDATE_INTERVAL = 5.0


class SimpleSlashTop:
    """Top bar, with 2 slashes on both ends, and transparent middle parts with Mpris2 widget at the center"""
    def __init__(self, colors) -> None:
        self.colors = colors
        self.highlight_method = 'line'

        # Widgets config
        widget_defaults.update({
            'background': colors.get('background_unfocus'),
            'foreground': colors.get('foreground')
        })

        launchbar_config = {
            'progs': [(' \u23fb ', "/home/xuantung/.config/rofi/scripts/powermenu_t2", "Power menu")],
            'default_icon': icons_path + 'system-devices-panel.svg',
            # 'text_only': True,
            'background': colors.get('cyan'),
            'padding': 2,
        }

        # Widgets
        separator = widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        size_percent=60,
                        padding=PAD*2
                    )

        groupbox_configs = dict(
            # padding_y=6,
            padding_x=8,
            background=colors.get('background_unfocus'),
            highlight_method=self.highlight_method,
            rounded=False,
            active=colors.get('foreground_focus'),
            inactive=colors.get('foreground_unfocus'),
            urgent_border=colors.get('urgent'),
            # for the focused screen
            this_current_screen_border=colors.get('background_focus'),
            other_current_screen_border=colors.get('background_other'),
            highlight_color=[_get_highlight_color(self.colors)],  # background for highlight_method='line'
            # for the other screen
            this_screen_border=colors.get('background_focus_noncurrent'),
            other_screen_border=colors.get('background_other'),
            disable_drag=True,
            use_mouse_wheel=False,
        )

        windowname_config = dict(
            foreground=colors.get('foreground_unfocus'),
            background=colors.get('background') + OPAQUE,
            fontsize=widget_defaults.get('fontsize') - 1,
            max_chars=40
        )

        tasklist_config = dict(
            foreground=colors.get('foreground_unfocus'),
            background=colors.get('background') + OPAQUE,
            fontsize=widget_defaults.get('fontsize') - 1,
            max_title_witdh=12
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
                        padding=1
                    )
        )

        widget_battery = (
            widget.BatteryIcon(
                theme_path=icons_path,
                **widget_defaults
            ),
            widget.Battery(
                # format='{char} {percent:2.0%}',
                # charge_char='',
                # discharge_char='',
                # empty_char='',
                # unknown_chFalsear='',
                format='{percent:2.0%}',
                **widget_defaults
            )
        )

        cpu_percentage = widget.CPU(
            format='󰻠 {load_percent}%',
            update_interval=UPDATE_INTERVAL,
            **widget_defaults
        )

        memory_usage = widget.Memory(
            format='{MemUsed: .2f}{mm}',
            measure_mem='G',
            update_interval=UPDATE_INTERVAL,
            **widget_defaults
        )

        mpris2 = widget.Mpris2(
                    foreground=colors.get('foreground_unfocus'),
                    background=colors.get('background') + OPAQUE,
                    padding=0,
                    fontsize=widget_defaults.get('fontsize') - 1,
                    scroll=True,
                    scroll_clear=True,
                    scroll_delay=1,
                    width=170,
                    name="spotify",
                    playing_text=" {track}",
                    paused_text=" Pause",
                    display_metadata=['xesam:title', 'xesam:artist'], # fMrmat='{xesam:title}',
                    objname="org.mpris.MediaPlayer2.spotify"
                )

        # screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(
                                        background=colors.get('background_unfocus'),
                                        fontsize=widget_defaults.get('fontsize') - 1,
                                        padding=5
                                ),
                        widget.GroupBox(
                            **groupbox_configs
                        ),
                        lower_left_triangle(foreground=colors.get('background_unfocus')),
                        widget.WindowName(
                            **windowname_config
                        ),
                        # widget.TaskList(
                        #     **tasklist_config
                        # ),
                        mpris2,
                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),
                        widget.Systray(
                            padding=5,
                            background=colors.get('background') + OPAQUE,
                            foreground=colors.get('background') + OPAQUE
                        ),
                        lower_right_triangle(foreground=colors.get('background_unfocus'),
                                             background=colors.get('background') + OPAQUE),
                        widget.ThermalSensor(
                            format=' {temp:.0f}{unit}',
                            tag_sensor="CPU",
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background_unfocus')[1:],
                            update_interval=UPDATE_INTERVAL),
                        separator,
                        cpu_percentage,
                        separator,
                        memory_usage,
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
                            format=" %b %d",
                            **widget_defaults
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+2
                        ),
                        widget.Clock(
                            format=" %H:%M",
                            **widget_defaults
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD+2
                        )
                        # widget.LaunchBar(**launchbar_config)
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
                            **groupbox_configs
                        ),
                        lower_left_triangle(foreground=colors.get('background_unfocus')),
                        widget.WindowName(
                            **windowname_config
                        ),
                        mpris2,
                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),
                        # widget.Clipboard(
                        #     foreground=colors.get('foreground_unfocus'),
                        #     background=colors.get('background_unfocus') + '00',
                        #     fontsize=widget_defaults.get('fontsize') - 1,
                        #     max_width=35,
                        #     timeout=None
                        # ),
                        lower_right_triangle(foreground=colors.get('background_unfocus')),
                        cpu_percentage,
                        separator,
                        memory_usage,
                        separator,
                        *widget_volume,
                        separator,
                        widget.Clock(
                            format=" %H:%M",
                            **widget_defaults,
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD
                        )
                        # widget.LaunchBar(**launchbar_config)
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
    colors_list = [colors.get('background_line_highlight'),
                   colors.get('background_unfocus'),
                   colors.get('background_other')]
    return next(color for color in colors_list if color is not None)

