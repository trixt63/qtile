import subprocess
import os

from libqtile import hook
from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()


# Auto start
@hook.subscribe.startup_once
def autostart():
    _autostart = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([_autostart])


# Auto restart
@hook.subscribe.startup
def autorestart():
    _autorestart = os.path.expanduser('~/.config/qtile/autorestart.sh')
    subprocess.Popen([_autorestart])
