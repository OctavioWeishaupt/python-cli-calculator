"""User input helpers with validation."""


from math import isfinite


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
            print('ERRO: Digite um número válido!')
        else:
            return number
