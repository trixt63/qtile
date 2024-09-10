import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.simple_slash_top import SimpleSlashTop
from modules.bar_styles.slash_top import SlashTop

from modules.colors.github_dark import GithubDark
from modules.colors.nord import Nord
from modules.colors.space_gray import SpaceGray
from modules.colors.gruvbox import Gruvbox

# colors = GithubDark()
# colors = Nord().colors
colors = SpaceGray().colors
# colors = Gruvbox()

# screens = SimpleSlashTop(colors=colors).screens
screens = SlashTop(colors=colors).screens
