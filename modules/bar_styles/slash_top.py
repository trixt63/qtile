from math import ceil, floor
from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles.decorators import *
from modules.widgets import widget_defaults


OPAQUE = '00'
icons_path = '/usr/share/icons/Papirus/22x22/panel/'
apps_icons_path = '/usr/share/icons/Papirus/'
# icons_path = '/usr/share/icons/Zafiro-Icons-Dark/panel/22/'
# apps_icons_path = '/usr/share/icons/Zafiro-Icons-Light/'
BARSIZE = 29
PAD = 9
_DECORATOR_PADDING = ceil(BARSIZE/10)
_DECORATOR_SIZE = ceil(BARSIZE*1.1 + 1) * 2
UPDATE_INTERVAL = 5.0


def _parse_text(text):
    for string in ["MongoDB Compass - "]:
        if text.startswith(string):
            text = text.replace(string, "")
            text = text + string[-3:] + string[:-3]
        return text


class SlashTop:
    def __init__(self, colors) -> None:
        self.colors = colors
        self.highlight_method = 'line'

        widget_defaults.update({
            'background': colors.get('background_unfocus'),
            'foreground': colors.get('foreground'), 
            'fontsize': floor(BARSIZE/2)
        })

        ######################
        #  Widgets & Params  #
        ######################
        separator = widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        size_percent=70,
                        padding=PAD*2 - 2
                    )

        _decorator_configs = dict(
                foreground=colors.get('background_unfocus'), 
                # fontsize=_DECORATOR_SIZE, 
                # padding=-_DECORATOR_PADDING
                fontsize=66, 
                padding=-3
                )
        _upper_left_triangle = upper_left_triangle(**_decorator_configs)
        _upper_right_triangle = upper_right_triangle(**_decorator_configs)
        _lower_left_triangle = lower_left_triangle(**_decorator_configs)

        groupbox_configs = dict(
            # padding_y=6,
            padding_x=PAD-1,
            background=colors.get('background_unfocus'),
            highlight_method=self.highlight_method,
            rounded=False,
            active=colors.get('foreground_focus'),
            inactive=colors.get('foreground_unfocus'),
            urgent_border=colors.get('urgent'),
            # for the focused screen
            this_current_screen_border=colors.get('background_focus'),
            other_curre_nt_screen_border=colors.get('background_alt'),
            highlight_color=[_get_highlight_color(self.colors)],  # background for highlight_method='line'
            # for the other screen
            this_screen_border=colors.get('background_focus_alt'),
            other_screen_border=colors.get('background_alt'),
            disable_drag=True,
            use_mouse_wheel=False,
        )

        windowname_config = dict(
            foreground=colors.get('background'),
            background=colors.get('background') + OPAQUE,
            fontsize=widget_defaults.get('fontsize') - 1,
            max_chars=36
        )

        tasklist_config = dict(
            # font='Lato',
            font=widget_defaults.get('font'),
            foreground=colors.get('background'),
            background=colors.get('background') + OPAQUE,
            fontsize=widget_defaults.get('fontsize') - 2,
            max_title_width=210,
            border=colors.get('background_focus'),
            # highlight_method='block',
            # border=colors.get('foreground'),
            highlight_method='border',
            borderwidth=1.5,
            icon_size=widget_defaults.get('fontsize') - 1,
            theme_mode='preferred',
            theme_path=apps_icons_path,
            margin=3,
            padding=3,
            parse_text=_parse_text,
            markup_focused='<span font_weight="600">{}</span>',
            markup_minimized='<span font_style="italic">_{}</span>',
            markup_maximized='<span>[] {}</span>'
        )

        MIDDLE_WIDGETS = [
            _upper_right_triangle,
            widget.Clock(
                format=" %H:%M",
                **widget_defaults
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=PAD*2 - 3
            ),
            widget.Clock(
                format=" %b %d",
                **widget_defaults
            ),
            _upper_left_triangle,
        ]

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
                        padding=0
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

        thermal_sensor = widget.ThermalSensor(
                            format=' {temp:.0f}{unit}',
                            tag_sensor="CPU",
                            foreground=colors.get('foreground')[1:],
                            background=colors.get('background_unfocus')[1:],
                            update_interval=UPDATE_INTERVAL)

        net = widget.Net(
            foreground = colors.get('foreground')[1:],
            background = colors.get('background_unfocus')[1:],
            format='󰓅 {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
            update_interval=UPDATE_INTERVAL
        )

        mpris2 = widget.Mpris2(
                    foreground=colors.get('background'),
                    background=colors.get('background') + OPAQUE,
                    padding=0,
                    fontsize=widget_defaults.get('fontsize') - 1,
                    scroll=True,
                    scroll_clear=True,
                    scroll_delay=1,
                    width=180,
                    name="spotify",
                    playing_text=" {track}",
                    paused_text=" Pause",
                    display_metadata=['xesam:title', 'xesam:artist'], # fMrmat='{xesam:title}',
                    objname="org.mpris.MediaPlayer2.spotify"
                )

        launchbar_config = {
            'progs': [(' \u23fb ', "/home/xuantung/.config/rofi/scripts/powermenu_t2", "Power menu")],
            'default_icon': icons_path + 'system-devices-panel.svg',
            # 'text_only': True,
            'background': colors.get('cyan'),
            'padding': 2,
        }
        #####################
        #      Screens      #
        #####################

        # Screen 1
        screen1 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(
                                        background=colors.get('background_unfocus'),
                                        fontsize=widget_defaults.get('fontsize') - 2,
                                        padding=4
                                ),
                        widget.GroupBox(
                            **groupbox_configs
                        ),
                        _upper_left_triangle,

                        # widget.WindowName(
                        #     **windowname_config
                        # ),
                        widget.TaskList(**tasklist_config),

                        *MIDDLE_WIDGETS,

                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),

                        mpris2,

                        _upper_right_triangle,
                        # thermal_sensor,
                        # separator,
                        cpu_percentage,
                        separator,
                        memory_usage,
                        separator,
                        *widget_volume,
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=(PAD - 2) * 2 - 3
                        ),
                        *widget_battery,
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=(PAD-2)*2 - 3
                        ),
                        # lower_left_triangle(foreground=colors.get('background_unfocus')),
                        _lower_left_triangle,
                        widget.Systray(
                            padding=5,
                            background=colors.get('background') + OPAQUE,
                            # foreground=colors.get('background')
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus') + OPAQUE,
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
        
        # Screen 2
        screen2 = Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(
                            background=colors.get('background_unfocus'),
                            fontsize=widget_defaults.get('fontsize') - 1,
                            padding=4
                        ),
                        widget.GroupBox(
                            **groupbox_configs
                        ),
                        _upper_left_triangle,

                        # widget.WindowName(
                        #     **windowname_config
                        # ),
                        widget.TaskList(**tasklist_config),

                        *MIDDLE_WIDGETS,

                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),

                        mpris2,
                        # widget.Clipboard(
                        #     foreground=colors.get('foreground_unfocus'),
                        #     background=colors.get('background_unfocus') + '00',
                        #     fontsize=widget_defaults.get('fontsize') - 1,
                        #     max_width=35,
                        #     timeout=None
                        # ),

                        _upper_right_triangle,
                        thermal_sensor,
                        separator,
                        cpu_percentage,
                        separator,
                        memory_usage,
                        separator,
                        *widget_volume,
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=(PAD - 2) * 2 - 3
                        ),
                        *widget_battery,
                        separator,
                        net,
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus'),
                            padding=PAD
                        ),
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
    colors_list = [colors.get('background_focus_highlight'),
                   colors.get('background_unfocus'),
                   colors.get('background_alt')]
    return next(color for color in colors_list if color is not None)

