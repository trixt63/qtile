class Nord:
    def __init__(self):
        self.black = '#2e3440'
        self.black2 = '#3b4252'
        self.black3 = '#434c5e'
        self.black4 = '#4c566a'
        self.white = '#eceff4'
        self.white2 = '#e5e9f0'
        self.white3 = '#d8dee9'
        self.white4 = '#9ea7b5'
        self.red = '#bf616a'
        self.yellow = '#ebcb8b'
        self.green = '#a3be8c'
        self.cyan = '#88c0d0'
        self.blue = '#81a1c1'
        self.purple = '#b48ead'
        # kinda redundance
        self.orange = '#d08770'
        self.cyan2 = '#8fbcbb'
        self.blue2 = '#5e81ac'

        self.colors = {
            'background': self.black,
            'foreground': self.white,

            'foreground_unfocus': self.blue,
            'background_unfocus': self.black2,

            'foreground_focus': self.white,
            'background_focus': self.cyan,

            'background_focus_noncurrent': self.blue2,  # focused workspace on unfocused monitor
            'background_other': self.black4,  # focused workspace of other monitor, on the focused monitor

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
    def background_other(self):
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
