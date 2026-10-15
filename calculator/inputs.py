"""User input helpers with validation."""


from math import isfinite
from calculator.ui import colorize


def read_number(prompt='Digite um valor: '):
    """Read a number from the user, asking again until it is valid.

    Accepts a comma as the decimal separator. Rejects text, empty
    input, and non-finite values such as nan and inf.

    Args:
        prompt: Text shown to the user when asking for input.

    Returns:
        The number entered by the user, as a float.
    """
    while True:
        try:
            raw = input(prompt)
            number = float(raw.replace(',', '.'))
            if not isfinite(number):
                raise ValueError
        except ValueError:
            print(colorize('ERRO: Digite um número válido!', 'red'))
        else:
            return number


def read_confirmation(prompt='Deseja continuar? [S/N] '):
    """Ask a yes/no question until the user gives a valid answer.

    Accepts 's' or 'n', in upper or lower case and with extra spaces.
    Any other answer, including an empty one, shows an error and asks
    again.

    Args:
        prompt: The question shown to the user.

    Returns:
        True if the user answered yes, False if the user answered no.
    """
    while True:
        choice = input(prompt).lower().strip()
        if choice not in ['s', 'n']:
            print(colorize('ERRO: Digite uma opção válida!', 'red'))
        else:
            return choice == 's'
