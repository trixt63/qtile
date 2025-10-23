from math import ceil, floor

from libqtile import layout
from libqtile.config import Match

from modules.screens import colors

MG = 6  # margin
BW = 5  # border width

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.MonadTall(margin=MG,
                     border_width=BW,
                     border_focus=colors.get('border_focus'),
                     border_normal=colors.get('border'),
                     single_border_width=0,
                     # single_margin=MG,
                     single_margin=0,
                     ratio=0.65),
    # Try more layouts by unleashing below layouts.
    # layout.Slice(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),

    layout.TreeTab(font="Lato",
                   fontsize=15,
                   panel_width=100,
                   # place_right=True,
                   vspace=5,
                   bg_color=colors.get('background'),
                   active_bg=colors.get('border_focus'),
                   urgent_bg=colors.get('urgent')
                   ),

    # layout.Max(margin=MG,
    #            border_width=BW,
    #            border_focus=colors.get('border_focus'),
    #            border_normal=colors.get('border')
    #            ),

    layout.Columns(num_colums=1,
                   insert_position=1,
                   border_width=BW,
                   border_on_single=True,
                   border_focus=colors.get('border_focus'),
                   border_normal=colors.get('border'),
                   margin=[MG, ceil(MG/2), MG, ceil(MG/2)],
                   margin_on_single=[MG]*4
                   ),
    # layout.VerticalTile(),
    # layout.Zoomy(columnwidth=100),
]

floating_layout = layout.Floating(
    border_focus=colors.get('border_focus'),
    border_normal=colors.get('black'),
    border_width=BW-2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="anki"),  # Anki
        Match(wm_class="goldendict"),  # GPG key password entry
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ], 
    no_reposition_rules=[
        # So that the pop-up follow the mouse. In GoldenDict preference for Popup: leave everything off, except Track Selection change.
        # also resize the floating windows as you wish
        Match(wm_class="goldendict"), 
    ]
)
