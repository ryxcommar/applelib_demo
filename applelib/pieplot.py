"""
The pieplot API lets you configure an Apple without ever setting one!

(Get it? "pie" plot... as in apple pie... oh, never mind.)
"""
from .config import get_current_apple
from copy import copy


def color(color: str) -> None:
    return get_current_apple().set_color(color)


def show():
    return copy(get_current_apple())
