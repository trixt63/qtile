class Gruvbox:
    def __init__(self):
        self.white = '#ffffff'
        self.black = '#000000'

        self.dark0_h = '#1d2021'
        self.dark0 = '#282828'
        self.dark0_s = '#32302f'
        self.dark1 = '#3c3836'
        self.dark2 = '#504945'
        self.dark3 = '#65737e'
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
        self.neutral_red = '#cc241d'
        self.neutral_green = '#98971a'
        self.neutral_yellow = '#d79921'
        self.neutral_blue = '#458588'
        self.neutral_purple = '#b16286'
        self.neutral_aqua = '#689d6a'
        self.neutral_orange = '#d65d0e'

        # dark mode colors
        self.bright_red = '#fb4934'
        self.bright_green = '#b8bb26'
        self.bright_yellow = '#fabd2f'
        self.bright_blue = '#83a598'
        self.bright_purple = '#d3869b'
        self.bright_aqua = '#8ec07c'
        self.bright_orange = '#fe8019'

        # light mode colors
        self.faded_red = '#9d0006'
        self.faded_green = '#79740e'
        self.faded_yellow = '#b57614'
        self.faded_blue = '#076678'
        self.faded_purple = '#8f3f71'
        self.faded_aqua = '#427b58'
        self.faded_orange = '#af3a03'

        self.colors = {
            # normal fg & bg
            'background': self.dark4,
            'foreground': self.light0,

            # groupbox fg & bg
            'foreground_unfocus': self.light0,
            'background_unfocus': self.dark0,

            'foreground_focus': self.white,
            'background_focus': self.neutral_yellow,
            'background_line_highlight': self.dark2,  # incase using highlight_method = line

            'background_focus_noncurrent': self.neutral_aqua,  # focused workspace on unfocused monitor
            'background_other': self.dark3,  # focused workspace of the other monitor (regardless if it's the focused or focused one)
            # 'background_alt': self.bg3,  # focused workspace of the other monitor (regardless if it's the focused or focused one)

            # border
            'border': self.dark0,
            'border_focus': self.neutral_yellow,

            'urgent': self.neutral_red,
        }

    def get(self, key, default=None):
        return self.colors.get(key, default)

    def __getitem__(self, key):
        return self.colors[key]
