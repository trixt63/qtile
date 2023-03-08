from .color_scheme import ColorScheme


class SpaceGray():
    def __init__(self):
        self.white0 = '#ffffff'
        self.black0 = '#000000'

        self.black = '#1c1f26'
        self.black2 = '#232830'
        # self.black3 = '#333d46'
        self.black3 = '#343d46'
        self.black4 = '#4f5b66'
        self.black5 = '#65737e'
        self.white = '#eff1f5'
        self.white2 = '#dfe1e8'
        self.white3 = '#c0c5ce'
        self.white4 = '#a7adba'

        self.red = '#bf616a'
        self.yellow = '#ebcb8b'
        self.cyan = '#96b5b4'
        self.yellow2 = '#fecc66'

        self.green = '#87b379'
        self.blue = '#7d8fa4'
        self.cyan2 = '#85A7A5'
        self.purple = '#a47996'


        self.colors = {
                'background': self.black2,
                'foreground': self.white,

                'foreground_unfocus': self.white4,
                'background_unfocus': self.black3,

                'foreground_focus': self.white0,
                'background_focus': self.yellow2,
                'background_focus_2': self.black4,  # incase using highlight_method = line

                'background_focus_alt': self.cyan,  # focused workspace on unfocused monitor
                'background_alt': self.black4,  # focused workspace of the other monitor

                'border': self.black2,
                'border_focus': self.yellow,

                'urgent': self.red,

                'red' :'#bf616a',
                'yellow': '#ebcb8b',
                'cyan': '#96b5b4',
                'blue': '#7d8fa4',
                'green': self.green
            }

    #
    # @property
    # def background(self):
    #     return self.black2
    #
    # @property
    # def foreground(self):
    #     return self.white
    #
    # @property
    # def foreground_unfocus(self):
    #     return self.white
    #
    # @property
    # def background_focus(self):
    #     return self.white
    #
    # @property
    # def foreground_focus(self):
    #     return self.black
    #
    # @property
    # def border(self):
    #     return self.black2
    #
    # @property
    # def border_focus(self):
    #     return self.yellow
    #
    # @property
    # def urgent(self):
    #     return self.red
    #
    # @property
    # def layout(self):
    #     return self.white2
    #
    # @property
    # def volume(self):
    #     return self.purple
    #
    # @property
    # def backlight(self):
    #     return self.blue
    #
    # @property
    # def battery(self):
    #     return self.cyan
    #
    # @property
    # def datetime(self):
    #     return self.green
    #
    # def systray(self):
    #     return self.black2
