class Kanagawa:
    def __init__(self):
        self.black_h = '#090618'
        self.black = '#16161d'
        self.black_s = '#1f1f28' # background
        self.black2 = '#727169'

        self.white = '#c8c093'
        self.white2 = '#dcd7ba'

        self.red = '#c34043'
        self.yellow = "#c0a36e"
        self.green = '#76946a'
        self.blue = '#7e9cd8'
        self.cyan = '#6a9589'
        self.magenta = '#957fb8'

        self.red2 = '#e82424'
        self.yellow2 = '#e6c384'
        self.green2 = '#98bb6c'
        self.blue2 = '#7fb4ca'
        self.cyan2 = '#7aa89f'
        self.magenta2 = '#938aa9'

        self.magenta3 = "#d27e99"
        self.orange = "#ffa066"
        self.orange2 = "#ff5d62"
        self.gray = '#2a2a37'  # base16 - base01
        self.gray2 = '#223249'  # base16 - base02
        self.gray3 = "#2D4F67"  # highlight-background-color
        self.blue3 = "#72A7BC"  # bold color

        # self._accent = self.orange
        # self._accent2 = self.magenta2
        self._accent = self.blue
        self._accent2 = self.green

        self.colors = {
            # normal fg & bg
            'background': self.black_s,
            'foreground': self.white2,

            # groupbox fg & bg
            'foreground_unfocus': self.white,
            'background_unfocus': self.black,

            'foreground_focus': self.white2,
            'background_focus': self._accent,
            'background_focus_noncurrent': self._accent2,  # focused workspace on unfocused monitor
            'background_other': self.black2,  # focused workspace of the other monitor (regardless of monitor )
            'background_line_highlight': self.gray,  # incase using highlight_method = line

            # border
            'border': self.gray,
            'border_focus': self._accent,

            'urgent': self.red2,

            # others
            'black': self.black,
            'red': self.red,
            'yellow': self.yellow,
            'cyan': self.cyan,
            'blue': self.blue,
            'green': self.green,
            'white': self.white,
            'magenta': self.magenta,
            'orange': self.orange
        }

    def get(self, color: str):
        return self.colors.get(color, None)

    def __getitem__(self, key):
        return self.colors[key]
