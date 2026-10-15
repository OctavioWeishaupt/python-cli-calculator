"""Terminal display helpers."""


LEN_LINE = 50
COLORS = {
    'reset': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'cyan': '\033[36m'
}

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


def format_expression(num1, symbol, num2, result):
    """Build the text of a calculation, such as '2 + 3 = 5'.

    Args:
        num1: The first number of the operation.
        symbol: The operation symbol (for example, '+').
        num2: The second number of the operation.
        result: The result of the operation.

    Returns:
        The calculation as text, with the three numbers formatted
        by format_number.
    """
    return f'{format_number(num1)} {symbol} {format_number(num2)} = {format_number(result)}'


def colorize(text, color):
    """Wrap a text in an ANSI color code.

    Args:
        text: The text to be colored.
        color: Name of the color: 'red', 'green', 'yellow' or 'cyan'.

    Returns:
        The text wrapped with the color code and the reset code.
    """
    return f'{COLORS[color]}{text}{COLORS["reset"]}'
