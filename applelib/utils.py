import re

VALID_COLOR_NAMES = [  # Not exhaustive
    'red',
    'green',
    'blue',
    'orange',
    'yellow',
    'purple',
    'black',
    'brown',
    'white',
    'pink'
]

VALID_COLOR_PATTERN = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'

def valid_color(color : str) -> bool:
    """
    Checks whether a string is a valid HTML color.
    Note: `VALID_COLOR_NAMES` does not include all named colors.
    """
    return (
        bool(re.match(VALID_COLOR_PATTERN, color))
        or (color in VALID_COLOR_NAMES)
    )
