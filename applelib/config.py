"""
Handle the global state of our apple manager.
"""

_current_apple = None


def get_current_apple() -> 'Apple':
    if _current_apple is None:
        from .apples import Apple
        set_current_apple(Apple())
    return _current_apple


def set_current_apple(apple: object) -> None:
    """Get the current apple from the global state."""
    globals()['_current_apple'] = apple
