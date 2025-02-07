from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy

from modules.keys import keys, mod

# Assign a value for _LABEL if you want all your groups share a label (e.g.: _LABEL = "")
# _LABEL = ''
_LABEL = None

groups = [
    Group("1", matches=[Match(wm_class=["firefox"])]),
    Group("2", matches=[
        Match(wm_class=["vscodium"]),
        Match(wm_class=["jetbrains-pycharm-ce"]),
        Match(wm_class=["jetbrains-pycharm"]),
        Match(wm_class=["jetbrains-rustrover"]),
        Match(wm_class=["jetbrains-webstorm"])
    ]),
    Group("3"),
    Group("4", matches=[
        Match(wm_class=["MongoDB Compass"]),
        Match(wm_class=["Postman"]),
        Match(wm_class=["pgadmin4"]),
        # Match(wm_class=["google-chrome"])
    ]),
    # Group("5", matches=[Match(wm_class=["libreoffice"]),
    #                     Match(wm_class=["calibre"])
    # ]),
    Group("5"),
    Group("6", matches=[
        Match(wm_class=["thunderbird-esr"]),
        Match(wm_class=["discord"])
    ]),
    Group("7", matches=[
        Match(wm_class=["Stremio"]),
        Match(wm_class=["spotify"])]),
    Group("8", matches=[
        Match(wm_class=["steam"]),
        Match(wm_class=["Lutris"])]),
    Group("9")
]

if _LABEL:
    for g in groups:
        g.label = _LABEL

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # # key(
            # #     [mod, "shift"],
            # #     i.name,
            # #     lazy.window.togroup(i.name, switch_group=true),
            # #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

