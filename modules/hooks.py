from libqtile import hook
import subprocess
import os


# Auto start
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# Auto restart
@hook.subscribe.startup
def autorestart():
    home = os.path.expanduser('~/.config/qtile/autorestart.sh')
    subprocess.Popen([home])
