"""In-memory history of the calculator operations."""

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
