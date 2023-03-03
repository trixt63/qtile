from modules.widgets import *


def lower_right_triangle(background=None,
                         foreground='#ffffff',
                         fontsize=60):
    return widget.TextBox(
        text='\u25E2',
        fontsize=fontsize,
        padding=-1,
        background=background,
        foreground=foreground
    )


def lower_left_triangle(background=None,
                        foreground='#ffffff',
                        fontsize=60):
    return widget.TextBox(
        text='\u25E3',
        fontsize=fontsize,
        padding=-1,
        background=background,
        foreground=foreground
    )


def upper_right_triangle(background=None,
                         foreground='#ffffff',
                         fontsize=58):
    return widget.TextBox(
        text='\u25E5',
        fontsize=fontsize,
        padding=0,
        background=background,
        foreground=foreground
    )


def left_triangle(background=None,
                  foreground='#ffffff',
                  fontsize=46):
    return widget.TextBox(
        text='\u25C0',
        fontsize=fontsize,
        padding=-1,
        background=background,
        foreground=foreground
    )


def right_triangle(background=None,
                  foreground='#ffffff',
                  fontsize=43):
    return widget.TextBox(
        text='\u25B6',
        fontsize=fontsize,
        padding=-1,
        background=background,
        foreground=foreground
    )
