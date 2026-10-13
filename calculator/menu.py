from calculator.ui import *

def show_menu():
    """
    -> Show the legend of handle choice
    """
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
    """
    -> Handle the choice
    :param option: receive user choice
    """
    match option:
        case '1':
            print('Opção ainda não disponível')
        case '2':
            print('Opção ainda não disponível')
        case '3':
            print('Opção ainda não disponível')
        case '4':
            print('Opção ainda não disponível')
        case '5':
            print('Opção ainda não disponível')
        case '6':
            print('Opção ainda não disponível')
        case '7':
            print('Opção ainda não disponível')
        case _:
            print('ERRO: Digite uma opção válida!')