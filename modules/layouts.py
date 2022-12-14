from libqtile import layout
from libqtile.config import Match

from .screens import colors

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.MonadTall(margin=4,
                     border_width=4,
                     border_focus=colors.border_focus,
                     border_normal=colors.border,
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
                   bg_color=colors.background,
                   active_bg=colors.background_focus,
                   urgent_bg=colors.urgent),
    # layout.Max(),
    layout.Columns(num_colums=1,
                   insert_position=1,
                   border_width=4,
                   border_focus=colors.border_focus,
                   border_normal=colors.border,
                   margin=[4, 2, 4, 2],
                   margin_on_single=[4, 4, 4, 4]
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