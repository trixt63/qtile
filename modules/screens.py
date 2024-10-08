import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.simple_slash_top import SimpleSlashTop
from modules.bar_styles.simple_slash import SimpleSlash
from modules.bar_styles.slash_top import SlashTop

from modules.colors.space_gray import SpaceGray
from modules.colors.gruvbox import Gruvbox


colors = SpaceGray().colors
screens = SlashTop(colors=colors).screens


# colors = Gruvbox()
# screens = SlashTop(colors=colors).screens
