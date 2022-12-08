from .color_scheme import ColorScheme


class GithubLight(ColorScheme):
    """Github light for Sublime Text
    Author: Mauro Reis Vieira <mauroreisvieira@gmail.com> 
    """
    def __init__(self):
        self.cursor = '#0969da'
        self.accent = '#fd8c73'
        self.black = '#24292f'
        self.black2 = '#32383f'
        self.black3 = '#57606a'  
        self.black4 = '#6e7781'
        self.white = '#ffffff'
        self.white2 = '#eaeef2'
        self.white3 = '#d0d7de'  
        self.white4 = '#8c959f'
        self.red = '#ff8182'
        self.yellow = '#fd8c73'
        self.green = '#4ac26b'
        self.cyan = '#76e3ea'
        self.blue = '#54aeff'
        self.purple = '#c297ff'

    @property
    def background(self):
        return self.white

    @property
    def foreground(self):
        return self.black

    @property
    def foreground_alt(self):
        """Unfocused group"""
        return self.white4

    @property
    def background_alt(self):
        """Unfocused group"""
        return self.white3

    @property
    def background_focus(self):
        return self.accent

    @property
    def foreground_focus(self):
        return self.black

    @property
    def border(self):
        return self.white3

    @property
    def border_focus(self):
        return '#0969da'

    @property
    def urgent(self):
        return '#cf222e' 
