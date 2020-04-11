APPLE_TEXT = [
    '    _ ',
    '   /  ',
    ' #### ',
    '######',
    '######',
    ' #### '
]

DEFAULT_APPLE_COLOR = 'red'

class NewApple(object):
    color = 'red'  # Default color is red

    def __init__(self, color: str = None):
        self.color: str = color or self.color

    def __repr__(self) -> str:
        return '\n'.join(APPLE_TEXT)

    def _repr_html_(self) -> str:
        """
        Special repr for Jupyter notebooks.
        """
        txt = '<br>'.join(APPLE_TEXT).replace(' ', '&nbsp')
        return f'<font color="{self.color}"><tt>{txt}</tt></font>'
