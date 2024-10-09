from math import ceil, floor
from libqtile import bar
from libqtile.config import Screen

from modules.bar_styles._decorators import *
from modules.widgets import widget_defaults
from modules.utils import get_firefox_instance
from modules.bar_styles._constants import ICONS_PATH, APPS_ICONS_PATH, UPDATE_INTERVAL

OPAQUE = '00'
BARSIZE = 30
PAD = 9
_DECORATOR_PADDING = ceil(BARSIZE/10)
_DECORATOR_SIZE = ceil(BARSIZE*1.1 + 1) * 2


class Cockpit:
    """Three-parted bar"""
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
            font=widget_defaults['font'],
            padding_x=PAD-1,
            background=colors.get('background_unfocus'),
            highlight_method=self.highlight_method,
            rounded=False,
            active=colors.get('foreground_focus'),
            inactive=colors.get('foreground_unfocus'),
            urgent_border=colors.get('urgent'),
            # for the focused screen
            this_current_screen_border=colors.get('background_focus'),
            other_current_screen_border=colors.get('background_alt'),
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
            # foreground=colors.get('foreground_unfocus'),
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
            theme_path=APPS_ICONS_PATH,
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
                        font="Font Awesome 6 Free Solid",
                        foreground=colors.get('foreground'),
                        background=colors.get('background_unfocus'),
                        padding=PAD/2-1,
                        emoji=True,
                        emoji_list=['', '', '', ''],
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
                theme_path=ICONS_PATH,
                **widget_defaults
            ),
            widget.Battery(
                format='{percent:2.0%}',
                **widget_defaults
            )
        )

        cpu_percentage = widget.CPU(
            format=' {load_percent}%',
            update_interval=UPDATE_INTERVAL,
            **widget_defaults
        )

        memory_usage = widget.Memory(
            format='󰘚{MemUsed: .2f}{mm}',
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

        # mpris2_all = widget.Mpris2(
        #             foreground=colors.get('background'),
        #             background=colors.get('background') + OPAQUE,
        #             padding=ceil(PAD),
        #             font=widget_defaults.get('font'),
        #             fontsize=widget_defaults.get('fontsize') - 2,
        #             fontshadow=colors.get('red'),
        #             scroll=True,
        #             scroll_clear=True,
        #             scroll_delay=1,
        #             width=180,
        #             # max_chars=20,
        #             name="mpris2",
        #             playing_text=" {track}",
        #             paused_text=' <span font_style="italic">{track}</span>',
        #             display_metadata=['xesam:title'], # fMrmat='{xesam:title}',
        #             poll_interval=0.5,
        #             objname=None
        #         )
        mpris2_firefox = widget.Mpris2(
                    background=colors.get('background') + OPAQUE,
                    foreground=colors.get('background'),
                    fontshadow=colors.get('red'),
                    # foreground=colors.get('red'),
                    padding=ceil(PAD),
                    font=widget_defaults.get('font'),
                    fontsize=widget_defaults.get('fontsize') - 3,
                    scroll=True,
                    scroll_clear=False,
                    scroll_delay=1,
                    width=140,
                    # max_chars=20,
                    name="firefox",
                    playing_text=" {track}",
                    paused_text=" Firefox",
                    no_metadata_text=" Firefox playing",
                    display_metadata=['xesam:title'],
                    poll_interval=1,  # prevent the widget from disappearing
                    objname=f"org.mpris.MediaPlayer2.{get_firefox_instance()}"
                )
        mpris2_spotify = widget.Mpris2(
                    background=colors.get('background') + OPAQUE,
                    foreground=colors.get('background'),
                    fontshadow=colors.get('green'),
                    # foreground=colors.get('green'),
                    padding=ceil(PAD/2),
                    font=widget_defaults.get('font'),
                    fontsize=widget_defaults.get('fontsize') - 3,
                    scroll=True,
                    scroll_clear=True,
                    scroll_delay=0.5,
                    width=150,
                    name="spotify",
                    playing_text=" {track}",
                    paused_text=" Spotify",
                    no_metadata_text=" Spotify playing",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    # poll_interval=1,
                    objname="org.mpris.MediaPlayer2.spotify"
                )
        mpris2 = [
                    mpris2_spotify, 
                    # widget.Sep(
                    #         linewidth=0,
                    #         size_percent=20,
                    #         background=colors.get('border')+OPAQUE,
                    #         foreground=colors.get('background'),
                    #         padding=int(PAD)
                    #     ),
                    # mpris2_firefox
                  ]

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
                                        padding=5
                                ),
                        widget.GroupBox(
                            **groupbox_configs
                        ),
                        _upper_left_triangle,

                        widget.TaskList(**tasklist_config),

                        *MIDDLE_WIDGETS,

                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),

                        *mpris2, 

                        _upper_right_triangle,
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
                        _lower_left_triangle,
                        widget.Systray(
                            padding=int(PAD/2)+1,
                            background=colors.get('background') + OPAQUE,
                            # foreground=colors.get('background')
                        ),
                        widget.Sep(
                            linewidth=0,
                            background=colors.get('background_unfocus') + OPAQUE,
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
        
        # Screen 2
        screen2 = Screen(
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
                        _upper_left_triangle,

                        widget.TaskList(**tasklist_config),

                        *MIDDLE_WIDGETS,

                        widget.Spacer(
                            background=colors.get('background') + OPAQUE,
                        ),

                        *mpris2,

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
                ),
            )

        self.screens = [
            screen1,
            screen2
        ]


def _parse_text(text):
    """remove redundant texts in some window names"""
    for string in ["MongoDB Compass - "]:
        if text.startswith(string):
            text = text.replace(string, "")
            text = text + string[-3:] + string[:-3]
        return text


def _get_highlight_color(colors):
    """Get the highlight_color (the background color) 
    for the GroupBox when highlight_method='line',
    in case the color scheme does not have 'background_focus_2'
    """
    colors_list = [colors.get('background_focus_highlight'),
                   colors.get('background_unfocus'),
                   colors.get('background_alt')]
    return next(color for color in colors_list if color is not None)
