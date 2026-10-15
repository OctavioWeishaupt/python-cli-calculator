"""In-memory history of the calculator operations."""

HISTORY_FILE = 'history.txt'
_entries = []


def add_entry(num1, symbol, num2, result):
    """Store one calculation in the history.

    Args:
        num1: The first number of the operation.
        symbol: The operation symbol (for example, '+').
        num2: The second number of the operation.
        result: The result of the operation.
    """
    _entries.append({'num1': num1, 'symbol': symbol, 'num2': num2, 'result': result})


def save_entry(num1, symbol, num2, result):
    """Append one calculation to the history file.

    The numbers are saved raw (not formatted), separated by ';',
    one calculation per line. The file is created if it does not exist.

    Args:
        num1: First operand.
        symbol: Operation symbol (e.g. '+', '**').
        num2: Second operand.
        result: Result of the operation.
    """
    line = f'{num1};{symbol};{num2};{result}\n'
    with open(HISTORY_FILE, 'a', encoding='utf-8') as file:
        file.write(line)


def get_entries():
    """Return a copy of the stored history.

    Returns:
        A new list with one dictionary per calculation, in the order
        they were made. Adding or removing items from this list does
        not affect the stored history.
    """
    return _entries.copy()


def clear_entries():
    """Remove all calculations from the stored history."""
    _entries.clear()


def _parse_line(line):
    """Convert one line of the history file into an entry dictionary.

    Args:
        line: A line in the format 'num1;symbol;num2;result', with or
            without the trailing newline.

    Returns:
        A dict with the keys 'num1', 'symbol', 'num2' and 'result'.
        The three numeric values are floats.
    """
    parts = line.strip().split(';')
    return {
        'num1': float(parts[0]),
        'symbol': parts[1],
        'num2': float(parts[2]),
        'result': float(parts[3])
    }
