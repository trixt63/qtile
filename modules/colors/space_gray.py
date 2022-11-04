from .color_scheme import ColorScheme


class SpaceGray(ColorScheme):
    def __init__(self):
        self.black = '#000000'
        self.black2 = '#20242d'
        self.black3='#4a4b4f'
        self.white = '#ffffff'
        self.white2 = '#b3b8c3'
        self.red = '#b04b57'
        self.yellow = '#e5c179'
        self.green = '#87b379'
        self.cyan = '#85a7a5'
        self.blue = '#7d8fa4'
        self.purple = '#a47996'

    @property
    def background(self):
        return self.black2

    @property
    def foreground(self):
        return self.white

    @property
    def foreground_alt(self):
        return self.white

    @property
    def background_focus(self):
        return self.white

    @property
    def foreground_focus(self):
        return self.black

    @property
    def border(self):
        return self.black2

    @property
    def border_focus(self):
        return self.yellow

    @property
    def urgent(self):
        return self.red

    @property
    def layout(self):
        return self.white2

    @property
    def volume(self):
        return self.purple

    @property
    def backlight(self):
        return self.blue

    @property
    def battery(self):
        return self.cyan

    @property
    def datetime(self):
        return self.green

    def systray(self):
        return self.black2