from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import keys, mod

# groups = [Group(i) for i in "123456789"]

groups = [
    Group("1", matches=[Match(wm_class=["Firefox-esr"])]),
    Group("2", matches=[
        Match(wm_class=["vscodium"]),
        Match(wm_class=["jetbrains-pycharm-ce"]),
        Match(wm_class=["jetbrains-pycharm"])]),
    Group("3"),
    Group("4", matches=[Match(wm_class=["Thunar"])]),
    Group("5", matches=[
        Match(wm_class=["MongoDB Compass"]),
        Match(wm_class=["Postman"])]),
    Group("6", matches=[Match(wm_class=["libreoffice"])]),
    Group("7", matches=[
        Match(wm_class=["thunderbird-default"]),
        Match(wm_class=["Microsoft Teams - Preview"]),
        Match(wm_class=["discord"])]),
    Group("8", matches=[Match(wm_class=["Spotify"])]),
    Group("9"),
]

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
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

