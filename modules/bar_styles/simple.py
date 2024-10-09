from math import ceil, floor
from libqtile import bar
from libqtile.config import Screen

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.layout.decorations import ConditionalBorder, GradientBorder, GradientFrame, RoundedCorners
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBox2, GroupBoxRule, ScreenRule


from modules.widgets import widget_defaults
from modules.utils import get_firefox_instance
from modules.bar_styles._constants import ICONS_PATH, APPS_ICONS_PATH, UPDATE_INTERVAL
from modules.bar_styles._decorators import lower_left_triangle, lower_right_triangle

OPAQUE = 'ff'
BARSIZE = 33
PAD = 9
_DECORATOR_PADDING = ceil(BARSIZE/10)
_DECORATOR_SIZE = ceil(BARSIZE*1.1 + 1) * 2


def set_label(rule, box):
    if box.focused:
        rule.text = "◉"
    elif box.occupied:
        rule.text = "◎"
    else:
        rule.text = "○"

    return True


GroupBoxRule().when(func=set_label)


class Simple:
    def __init__(self, colors):
        self.colors = colors
        self.highlight_method = 'block'

        widget_defaults.update({
            'padding': 10
        })

        # widgets
        current_layout_icon = widget.CurrentLayoutIcon(
            background=colors.get('background_unfocus'),
            fontsize=widget_defaults.get('fontsize') - 1,
            padding=7
        )

        clock = widget.Clock(
                format=" %H:%M",
                **widget_defaults
        )

        _groupbox_config = dict(
            # use _LABEL for group
            fontsize=15,
            foreground=colors.get('foreground'),
            background=colors.get('background'),
            highlight_method='text',
            borderwidth=3,
            padding=7,
            disable_drag=True,
            # colors
            active=colors.get('foreground_focus'),
            inactive=colors.get('foreground_unfocus'),
            # on the focused screen
            this_current_screen_border=colors.get('background_focus'),
            other_current_screen_border=colors.get('background_alt'),
            # on the not focused screen(s)
            this_screen_border=colors.get('background_focus_alt'),
            other_screen_border=colors.get('background_alt'),

            # block_highlight_text_color=colors['orange'],
            # highlight_color=colors.get("background_unfocus"),

            # deco
            decorations=[rectdeco(colors['background_unfocus'])]
        )
        groupbox = widget.GroupBox(**_groupbox_config)

        _groupbox2_config = dict(
            fontsize=20,
            padding_x=5,
            rules=[
                  GroupBoxRule().when(func=set_label),
                  GroupBoxRule(text_colour=colors['background_focus']).when(screen=ScreenRule.THIS),
                  GroupBoxRule(text_colour=colors['background_focus_alt']).when(screen=ScreenRule.OTHER),
                  GroupBoxRule(text_colour=colors['background_alt'][1:]).when()
            ]
        )
        groupbox2_1 = widget.GroupBox2(**_groupbox2_config)
        groupbox2_2 = widget.GroupBox2(**_groupbox2_config)

        _tasklist_config = dict(
            # font='Lato',
            font=widget_defaults.get('font'),
            foreground=colors.get('background'),
            # foreground=colors.get('foreground_unfocus'),
            background=colors.get('background') + OPAQUE,
            fontsize=widget_defaults.get('fontsize') - 2,
            max_title_width=210,
            border=colors.get('background_focus'),
            highlight_method='block',
            # border=colors.get('foreground'),
            # highlight_method='border',
            # borderwidth=1.5,
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
        tasklist = widget.TaskList(**_tasklist_config)

        widgets_list = [
            current_layout_icon,
            # groupbox,
            groupbox2_1,
            tasklist,
            widget.Mpris2(
                foreground=colors.get('foreground_unfocus'),
                padding=0,
                fontsize=widget_defaults.get('fontsize') - 1,
                max_chars=35,
                name="spotify",
                playing_text=' {track}',
                paused_text=" Pause",
                # format="{xesam:title} - {xesam:artist}",
                display_metadata=["xesam:title", "xesam:artist"],
                objname="org.mpris.MediaPlayer2.spotify"
            ),
            lower_right_triangle(foreground=colors.get('background_unfocus')),
            # widget.ThermalSensor(
            #     format=' {temp:.0f}{unit}',
            #     foreground=colors.get('foreground')[1:],
            #     background=colors.get('background_unfocus')[1:],
            #     update_interval=UPDATE_INTERVAL,
            #     padding=PAD
            # ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=PAD + 1
            ),
            widget.CPU(
                format=' {load_percent}%',
                foreground=colors.get('foreground')[1:],
                background=colors.get('background_unfocus')[1:],
                padding=0,
                update_interval=UPDATE_INTERVAL,
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=PAD + 1
            ),
            widget.Memory(
                format=' {MemUsed:.2f}{mm}',
                measure_mem='G',
                foreground=colors.get('foreground')[1:],
                background=colors.get('background_unfocus')[1:],
                padding=PAD,
                update_interval=UPDATE_INTERVAL,
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=PAD - 2
            ),
            widget.Volume(
                padding=2,
                # theme_path=icons_path,
                emoji=True,
                background=colors.get('background_unfocus')[1:],
            ),
            widget.Volume(
                fmt='{}',
                padding=2,
                background=colors.get('background_unfocus')[1:],
                foreground=colors.get('foreground')[1:],
            ),

            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=PAD
            ),
            widget.Clock(
                # format=" %a, %b %d   %H:%M",
                format=" %b %d   %H:%M",
                # font='Font Awesome 5 Free Solid',
                padding=PAD,
                background=colors.get('background_unfocus'),
                foreground=colors.get('foreground'),
            ),
            widget.Systray(
                padding=6,
                background=colors.get('background_unfocus'),
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=int(PAD / 3)
            ),
            widget.LaunchBar(
                progs=[('Power', "/home/xuantung/.config/rofi/bin/menu_powermenu", "Power menu")],
                default_icon='/usr/share/icons/Papirus/22x22/panel/system-devices-panel.svg',
                background=colors.get('background_unfocus'),
                foreground=colors.get('foreground'),
                padding=int(PAD / 3)
            ),
            widget.Sep(
                linewidth=0,
                background=colors.get('background_unfocus'),
                padding=int(PAD / 3)
            ),
            # widget.QuickExit(),
        ]

        # screen 1
        screen1 = Screen(
            top=bar.Bar(
                widgets=widgets_list,
                size=BARSIZE,
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
                    # widget.GroupBox(
                    #     **_groupbox_config
                    # ),
                    groupbox2_2,
                    lower_left_triangle(foreground=colors.get('background_unfocus')),
                    widget.WindowName(
                        foreground=colors.get('foreground_unfocus'),
                        # padding=12,
                        fontsize=widget_defaults.get('fontsize') - 1,
                        max_chars=50
                    ),
                    widget.Mpris2(
                        foreground=colors.get('foreground_unfocus'),
                        fontsize=widget_defaults.get('fontsize') - 1,
                        padding=0,
                        scroll=True,
                        scroll_clear=True,
                        width=185,
                        name="spotify",
                        playing_text=" {track}",
                        paused_text=" Pause",
                        display_metadata=["xesam:title", "xesam:artist"],
                        objname="org.mpris.MediaPlayer2.spotify"
                    ),
                    widget.Spacer(
                        background=colors.get('background'),
                    ),
                    widget.Clipboard(
                        foreground=colors.get('foreground_unfocus'),
                        max_width=30,
                        timeout=None
                    ),
                    lower_right_triangle(foreground=colors.get('background_unfocus')),
                    widget.Volume(
                        padding=1,
                        # theme_path=icons_path,
                        emoji=True,
                        background=colors.get('background_unfocus')[1:],
                        foreground=colors.get('foreground')[1:],
                    ),
                    widget.Volume(
                        fmt='{}',
                        padding=1,
                        background=colors.get('background_unfocus')[1:],
                        foreground=colors.get('foreground')[1:],
                    ),
                    widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        padding=12
                    ),
                    widget.Clock(
                        format=" %H:%M",
                        # font='Font Awesome 5 Free Solid',
                        padding=PAD,
                        background=colors.get('background_unfocus'),
                        foreground=colors.get('foreground'),
                    ),
                    widget.LaunchBar(
                        progs=[('Power', "/home/xuantung/.config/rofi/bin/menu_powermenu", "Power menu")],
                        default_icon='/usr/share/icons/Papirus/22x22/panel/system-devices-panel.svg',
                        background=colors.get('background_unfocus'),
                        foreground=colors.get('foreground'),
                        padding=int(PAD / 3)
                    ),
                    widget.Sep(
                        linewidth=0,
                        background=colors.get('background_unfocus'),
                        padding=int(PAD / 3)
                    ),
                ],
                BARSIZE,
                background=colors.get('background'),
            ),
        )
        self.screens = [
            screen1,
            screen2
        ]


def rectdeco(hexcolor):
    return RectDecoration(
        filled=True,
        colour=hexcolor,
        padding_y= 5,
        padding_x= 0,
        radius=4
    )


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
    colors_list = [colors.get('background_focus_2'),
                   colors.get('background_unfocus'),
                   colors.get('background_alt')]
    return next(color for color in colors_list if color is not None)
