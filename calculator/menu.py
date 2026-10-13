"""Main menu display and option handling."""


from calculator.inputs import read_number
from calculator.ui import title, line
from calculator.operations import add, subtract, multiply, divide, power


def show_menu():
    """Print the main menu with all available options."""
    title('CALCULADORA PYTHON')
    print('  [ 1 ] - Somar')
    print('  [ 2 ] - Subtrair')
    print('  [ 3 ] - Multiplicar')
    print('  [ 4 ] - Dividir')
    print('  [ 5 ] - Potência')
    print('  [ 6 ] - Ver histórico')
    print('  [ 7 ] - Limpar histórico')
    print('  [ 0 ] - Sair')
    line()


def handle_choice(option):
    """Run the action that matches the chosen menu option.

    Args:
        option: The option typed by the user, as a string.
    """
    match option:
        case '1':
            a = read_number('Primeiro número: ')
            b = read_number('Segundo número: ')
            try:
                result = add(a, b)
            except OverflowError:
                print('ERRO: Resultado grande demais.')
            else:
                print(f'Resultado: {result}')
        case '2':
            a = read_number('Primeiro número: ')
            b = read_number('Segundo número: ')
            try:
                result = subtract(a, b)
            except OverflowError:
                print('ERRO: Resultado grande demais.')
            else:
                print(f'Resultado: {result}')
        case '3':
            a = read_number('Primeiro número: ')
            b = read_number('Segundo número: ')
            try:
                result = multiply(a, b)
            except OverflowError:
                print('ERRO: Resultado grande demais.')
            else:
                print(f'Resultado: {result}')
        case '4':
            a = read_number('Numerador: ')
            b = read_number('Denominador: ')
            try:
                result = divide(a, b)
            except OverflowError:
                print('ERRO: Resultado grande demais.')
            except ZeroDivisionError:
                print('ERRO: Divisão por zero não é permitida.')
            else:
                print(f'Resultado: {result}')
        case '5':
            a = read_number('Base: ')
            b = read_number('Expoente: ')
            try:
                result = power(a, b)
            except OverflowError:
                print('ERRO: Resultado grande demais.')
            except ZeroDivisionError:
                print('ERRO: Zero não pode ser elevado a um número negativo.')
            except ValueError:
                print('ERRO: Resultado não é real.')
            else:
                print(f'Resultado: {result}')
        case '6':
            print('Opção ainda não disponível')
        case '7':
            print('Opção ainda não disponível')
        case _:
            print('ERRO: Digite uma opção válida!')