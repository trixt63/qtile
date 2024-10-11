from .color_scheme import ColorScheme


class GithubDark(ColorScheme):
    def __init__(self):
        self.black = '#0d1117'
        self.black2 = '#161b22'
        self.black3 = '#21262d'
        self.black4 = '#33373d'
        self.white = '#ecf2f8'
        self.white2 = '#c6cdd5'
        self.white3 = '#89929b'
        self.white4 = '#6a7785'
        self.red = '#fa7970'
        self.yellow = '#faa356'
        self.green = '#7ce38b'
        self.cyan = '#a2d2fb'
        self.blue = '#77bdfb'
        self.purple = '#cea5fb'

        self.colors = {
            'background': self.black,
            'foreground': self.white,
            'foreground_unfocus': self.white3,
            'background_unfocus': self.black2,
            'foreground_focus': self.white,
            'background_focus': self.blue,
            'background_focus_noncurrent': self.blue2,
            'background_other': self.black4,
            'border': self.black3,
            'border_focus': self.blue,
            'urgent': self.red,
        }

    @property
    def background(self):
        return self.black

    @property
    def foreground(self):
        return self.white

    @property
    def foreground_unfocus(self):
        """Unfocused group"""
        return self.white3

    @property
    def background_unfocus(self):
        """Unfocused group"""
        return self.black4

    @property
    def background_focus(self):
        return self.blue

    @property
    def foreground_focus(self):
        return self.white

    @property
    def border(self):
        return self.black3

    @property
    def border_focus(self):
        return self.blue

    @property
    def urgent(self):
        return self.red
