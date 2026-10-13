from math import isfinite

def read_number(prompt='Digite um valor: '):
    """
    -> Read a number from the user.
    :param prompt: The prompt to be displayed
    :return: Return the entered number if valid
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
