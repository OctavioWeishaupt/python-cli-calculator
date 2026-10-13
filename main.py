"""Entry point of the CLI calculator."""


from calculator.menu import show_menu, handle_choice
from calculator.ui import title


def main():
    """Run the main menu loop until the user chooses to exit."""
    while True:
        show_menu()
        user_choice = input("Escolha uma opção: ")
        if user_choice == '0':
            break
        else:
            handle_choice(user_choice)
    title('FINALIZANDO ...')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Programa interrompido pelo usuário.')
        title('FINALIZANDO ...')
    except EOFError:
        print()
        print('Entrada encerrada pelo usuário.')
        title('FINALIZANDO ...')
