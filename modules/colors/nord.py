from .color_scheme import ColorScheme


class Nord(ColorScheme):
    def __init__(self):
        self.black = '#2e3440'
        self.black2 = '#3b4252'
        self.black3 = '#434c5e'
        self.black4 = '#4c566a'
        self.white = '#eceff4'
        self.white2 = '#e5e9f0'
        self.white3 = '#d8dee9'
        self.red = '#bf616a'
        self.yellow = '#d08770'
        self.green = '#a3be8c'
        self.cyan = '#8fbcbb'
        self.blue = '#81a1c1'
        self.purple = '#b48ead'
        # kinda redundance
        self.cyan2 = '#88c0d0'
        self.blue2 = '#5e81ac'

        self.colors = {
            'background': self.black,
            'foreground': self.white,
            'foreground_unfocus': self.blue,
            'background_unfocus': self.black2,
            'foreground_focus': self.white,
            'background_focus': self.cyan,
            'background_focus_alt': self.blue2,
            'background_alt': self.black4,
            'border': self.black3,
            'border_focus': self.yellow,
            'urgent': self.red,
        }

    @property
    def background(self):
        return self.black

    @property
    def foreground(self):
        return self.white

    @property
    def background_alt(self):
        return self.black4

    @property
    def background_focus_alt(self):
        return self.blue2

    @property
    def foreground_unfocus(self):
        """Unfocused group"""
        return self.blue

    @property
    def background_unfocus(self):
        """Unfocused group"""
        return self.black2

    @property
    def background_focus(self):
        return self.cyan

    @property
    def foreground_focus(self):
        return self.white

    @property
    def border(self):
        return self.black3

    @property
    def border_focus(self):
        return self.yellow

    @property
    def urgent(self):
        return self.red
