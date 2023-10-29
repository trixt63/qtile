import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.round_top import RoundTop
from modules.bar_styles.simple_slash_top import SimpleSlashTop
from modules.colors.github_dark import GithubDark
from modules.colors.nord import Nord
from modules.colors.space_gray import SpaceGray

# colors = GithubDark()
# colors = Nord().colors
# colors_dict = colors.colors
colors = SpaceGray().colors

screens = SimpleSlashTop(colors=colors).screens
# screens = RoundTop(colors=colors).screens
