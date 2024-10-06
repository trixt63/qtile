# from .color_scheme import ColorScheme


class SpaceGray:
    def __init__(self):
        self.white0 = '#ffffff'
        self.black0 = '#000000'

        self.black1 = '#1c1f26'
        self.black2 = '#232830'
        self.black3 = '#333d46'
        self.black4 = '#343d46'
        self.black5 = '#4f5b66'

        self.white1 = '#eff1f5'
        self.white2 = '#dfe1e8'
        self.white3 = '#c0c5ce'
        self.white4 = '#a7adba'
        self.white5 = '#65737e'

        self.red = '#bf616a'
        self.yellow = '#ebcb8b'
        self.green = '#87b379'
        self.blue = '#7d8fa4'
        self.cyan = '#96b5b4'
        self.magenta = '#a47996'

        self.orange = '#c5735e'
        self.grey = "#4b5056"

        self.yellow2 = '#fecc66'
        self.cyan2 = '#85A7A5'

        self.colors = {
            # normal fg & bg
            'background': self.black2,
            'foreground': self.white1,

            # groupbox fg & bg
            'foreground_unfocus': self.white4,
            'background_unfocus': self.black3,
            'foreground_focus': self.white0,
            'background_focus': self.yellow2,
            'background_focus_highlight': self.black5,  # incase using highlight_method = line

            'background_focus_alt': self.cyan,  # focused workspace on unfocused monitor
            'background_alt': self.white5,  # focused workspace of the other monitor (regardless if it's the focused or focused one)

            # border
            'border': self.black3,
            'border_focus': self.yellow2,

            'urgent': self.red,

            # others
            'black': self.black1,
            'red': self.red,
            'yellow': self.yellow,
            'cyan': self.cyan,
            'blue': self.blue,
            'green': self.green,
            'white': self.white1,
            'magenta': self.magenta,
            'orange': self.orange
        }

    def get(self, color: str):
        return self.colors.get(color, None)

    def __getitem__(self, key):
        return self.colors[key]
