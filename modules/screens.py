import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.silver_blade2 import SilverBlades2
from modules.bar_styles.silver_blade1 import SilverBlades1
from modules.bar_styles.simple_slash import SimpleSlash
from modules.colors.github_dark import GithubDark
from modules.colors.github_light import GithubLight

colors = GithubDark()
# colors = GithubLight()

# screens = SimpleSlash(colors=colors).screens
screens = SimpleSlash(colors=colors).screens
