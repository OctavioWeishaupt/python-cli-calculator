from calculator.menu import show_menu, handle_choice, title


def main():
    while True:
        show_menu()
        user_choice = input("Escolha uma opção: ")
        if user_choice == '0':
            break
        else:
            handle_choice(user_choice)
    title('FINALIZANDO ...')


if __name__ == '__main__':
    main()