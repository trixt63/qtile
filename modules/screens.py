import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.simple_slash_top import SimpleSlashTop
from modules.bar_styles.simple_slash import SimpleSlash
from modules.bar_styles.cockpit import Cockpit
from modules.bar_styles.simple_buds import SimpleBuds

from modules.colors.space_gray import SpaceGray
from modules.colors.gruvbox import Gruvbox


colors = SpaceGray().colors
# colors = Gruvbox().colors

# screens = Cockpit(colors=colors).screens
screens = SimpleBuds(colors=colors).screens
