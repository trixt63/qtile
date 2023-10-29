from modules.widgets import *
# from libqtile import drawer


"""Some how, lower triangles can't use Nerd font character, 
so I'm stuck with standard unicode characters for the following 2"""
def lower_right_triangle(background=None,
                         foreground='#ffffff',
                         fontsize=65):
    return widget.TextBox(
        text='\u25E2',
        fontsize=fontsize,
        padding=-3,
        background=background,
        foreground=foreground
    )


def lower_left_triangle(background=None,
                        foreground='#ffffff',
                        fontsize=65):
    return widget.TextBox(
        text='\u25E3',
        fontsize=fontsize,
        padding=-3,
        background=background,
        foreground=foreground
    )


"""These 2 use Nerd font characters tho"""
def left_triangle(background=None,
                  foreground='#ffffff',
                  fontsize=44):
    return widget.TextBox(
        text='\uf438',
        # text='\u25C0',  # unicode character
        fontsize=fontsize,
        padding=-5,
        background=background,
        foreground=foreground
    )


def right_triangle(background=None,
                  foreground='#ffffff',
                  fontsize=43):
    return widget.TextBox(
        text='\uf44a',
        # text='\u25B6',  # unicode chracter
        fontsize=fontsize,
        padding=-5,
        background=background,
        foreground=foreground
    )

def left_half_circle(background=None,
                     foreground='#ffffff',
                     fontsize=43,
                     padding=-5):
    return widget.TextBox(
        text='\u25D7',
        fontsize=fontsize,
        padding=padding,
        background=background,
        foreground=foreground
    )

def right_half_circle(background=None,
                      foreground='#ffffff',
                      fontsize=43,
                      padding=-5):
    return widget.TextBox(
        text='\u25D6',
        fontsize=fontsize,
        padding=padding,
        background=background,
        foreground=foreground
    )
