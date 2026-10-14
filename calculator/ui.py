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


def format_number(num):
    """Format a number for display in the terminal.

    Rounds to 6 decimal places and removes trailing zeros. Whole numbers
    are shown without a decimal point, and tiny values that round to zero
    are shown as 0 (never -0).

    Args:
        num: The number to format.

    Returns:
        The formatted number as a string.
    """
    num = round(num, 6)
    if num.is_integer():
        return str(int(num))
    else:
        txt_num = f'{num:.6f}'
        return txt_num.rstrip('0').rstrip('.')
