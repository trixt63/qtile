from math import ceil

from libqtile import layout
from libqtile.config import Match

from .screens import colors

MG = 5  # margin
BW = 3  # border width

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.MonadTall(margin=MG,
                     border_width=BW,
                     border_focus=colors.get('border_focus'),
                     border_normal=colors.get('border'),
                     single_border_width=0,
                     single_margin=0,
                     ratio=0.6),
    # Try more layouts by unleashing below layouts.
    # layout.Slice(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(font="Lato",
                   fontsize=15,
                   panel_width=110,
                #    place_right=True,
                   vspace=6,
                   bg_color=colors.get('background'),
                   active_bg=colors.get('background_focus'),
                   urgent_bg=colors.get('urgent')),
    # layout.Max(),
    layout.Columns(num_colums=1,
                   insert_position=1,
                   border_width=BW,
                   border_focus=colors.get('border_focus'),
                   border_normal=colors.get('border'),
                   margin=[MG, ceil(MG/2), MG, ceil(MG/2)],
                   margin_on_single=[MG, MG, MG, MG]
                   )
    # layout.VerticalTile(),
    # layout.Zoomy(columnwidth=100),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
