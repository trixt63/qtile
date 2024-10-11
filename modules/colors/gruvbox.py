class Gruvbox:
    def __init__(self):
        self.dark0_hard = '#1d2021'
        self.dark0 = '#282828'
        self.dark0_soft = '#32302f'
        self.dark1 = '#3c3836'
        self.dark2 = '#504945'
        self.dark3 = '#665c54'
        self.dark4 = '#7c6f64'

        self.gray = '#928374'

        self.light0_hard = '#f9f5d7'
        self.light0 = '#fbf1c7'
        self.light0_soft = '#f2e5bc'
        self.light1 = '#ebdbb2'
        self.light2 = '#d5c4a1'
        self.light3 = '#bdae93'
        self.light4 = '#a89984'

        # standard colors
        self.red = '#cc241d'
        self.green = '#98971a'
        self.yellow = '#d79921'
        self.blue = '#458588'
        self.purple = '#b16286'
        self.aqua = '#689d6a'
        self.gray = '#a89984'
        self.orange = '#d65d0e'

        # dark mode colors
        self.red2 = '#fb4934'
        self.green2 = '#b8bb26'
        self.yellow2 = '#fabd2f'
        self.blue2 = '#83a598'
        self.purple2 = '#d3869b'
        self.aqua2 = '#8ec07c'
        self.gray2 = '#928374'
        self.orange2 = '#fe8019'

        # light mode colors
        # self.faded_red = '#9d0006'
        # self.faded_green = '#79740e'
        # self.faded_yellow = '#b57614'
        # self.faded_blue = '#076678'
        # self.faded_purple = '#8f3f71'
        # self.faded_aqua = '#427b58'
        # self.faded_orange = '#af3a03'

        self._accent = self.green2

        self.colors = {
            # normal fg & bg
            'background': self.dark0,
            'foreground': self.light0,

            # groupbox fg & bg
            'foreground_unfocus': self.light4,
            'background_unfocus': self.dark0_soft,

            'foreground_focus': self.light0,
            'background_focus': self._accent,
            'background_line_highlight': self.dark2,  # incase using highlight_method = line

            'background_focus_noncurrent': self.blue,  # focused workspace on unfocused monitor
            'background_other': self.dark3,  # focused workspace of the other monitor (regardless if it's the focused or focused one)

            # border
            'border': self.dark0,
            'border_focus': self._accent,

            'urgent': self.red,
        }

    def get(self, key, default=None):
        return self.colors.get(key, default)

    def __getitem__(self, key):
        return self.colors[key]
