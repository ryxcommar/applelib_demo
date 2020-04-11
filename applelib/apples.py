from .config import set_current_apple
from .utils import valid_color

APPLE_TEXT = [
    '    _ ',
    '   /  ',
    ' #### ',
    '######',
    '######',
    ' #### '
]

class Apple(object):
    _color = DEFAULT_APPLE_COLOR

    def __init__(self, color: str = None):
        self._color: str = color or self._color
        set_current_apple(self)  # <-- We'll get back to this later.

    def set_color(self, color: str) -> None:
        if valid_color(color):
            self._color = color
        else:
            raise ValueError(
                f'{color.__repr__()} is not a valid color.'
            )

    @property
    def color(self) -> str:
        return self._color

    def __repr__(self) -> str:
        return '\n'.join(APPLE_TEXT)

    def _repr_html_(self) -> str:
        """
        Special repr for Jupyter notebooks.
        """
        txt = '<br>'.join(APPLE_TEXT).replace(' ', '&nbsp')
        return f'<font color="{self.color}"><tt>{txt}</tt></font>'
