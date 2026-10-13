"""Terminal display helpers."""


LEN_LINE = 50


def line():
    """Print a horizontal separator line."""
    print('-' * LEN_LINE)


def title(txt):
    """Print a text centered between two separator lines.

    Args:
        txt: The title text to display.
    """
    line()
    print(txt.center(LEN_LINE))
    line()