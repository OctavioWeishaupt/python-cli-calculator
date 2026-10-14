"""Main menu display and option handling."""


from calculator.inputs import read_number
from calculator.ui import title, line, format_expression
from calculator.operations import add, subtract, multiply, divide, power
from calculator.history import add_entry, get_entries

OPERATIONS = {
    '1': {
        'func': add,
        'prompt_a': 'Primeiro número: ',
        'prompt_b': 'Segundo número: ',
        'symbol': '+'
    },
    '2': {
        'func': subtract,
        'prompt_a': 'Primeiro número: ',
        'prompt_b': 'Segundo número: ',
        'symbol': '-'
    },
    '3': {
        'func': multiply,
        'prompt_a': 'Primeiro número: ',
        'prompt_b': 'Segundo número: ',
        'symbol': '×'
    },
    '4': {
        'func': divide,
        'prompt_a': 'Numerador: ',
        'prompt_b': 'Denominador: ',
        'symbol': '÷'
    },
    '5': {
        'func': power,
        'prompt_a': 'Base: ',
        'prompt_b': 'Expoente: ',
        'symbol': '^'
    }
}


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


def show_history():
    """Show the calculation history on the screen.

    Prints every saved calculation, numbered from 1, in the order they
    were made. If nothing has been saved yet, shows a message saying
    the history is empty.
    """
    entries = get_entries()
    if entries:
        title('HISTÓRICO:')
        for index, entry in enumerate(entries, start=1):
            print(f'{index}. {format_expression(entry['num1'], entry['symbol'], entry['num2'], entry['result'])}')
        line()
    else:
        title('Histórico vazio.')


def run_operation(operation):
    """Run one calculator operation from start to finish.

    Asks the user for two numbers, calculates the result and shows the
    full expression (for example, 2 + 3 = 5). Successful calculations
    are also saved in the history. If the calculation fails, shows an
    error message instead and nothing is saved.

    Args:
        operation: A dictionary with the data of one operation, from
            OPERATIONS (function, prompts and symbol).
    """
    a = read_number(operation['prompt_a'])
    b = read_number(operation['prompt_b'])
    try:
        result = operation['func'](a, b)
    except OverflowError:
        print('ERRO: Resultado grande demais.')
    except ZeroDivisionError:
        print('ERRO: Operação indefinida (divisão por zero).')
    except ValueError:
        print('ERRO: Resultado não é real.')
    else:
        print(format_expression(a, operation['symbol'], b, result))
        add_entry(a, operation['symbol'], b, result)


def handle_choice(option):
    """Run the action that matches the chosen menu option.

    Args:
        option: The option typed by the user, as a string.
    """
    match option:
        case '1' | '2' | '3' | '4' | '5':
            run_operation(OPERATIONS[option])
        case '6':
            show_history()
        case '7':
            print('Opção ainda não disponível')
        case _:
            print('ERRO: Digite uma opção válida!')