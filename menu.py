def display_main_menu():
    """Отображение главного меню"""

    print("1. Все аудиозаписи (исполнитель↑, год↓, прослушивания↓)")
    print("2. Записи конкретного исполнителя (альбом↓, название↑)")
    print("3. Записи по диапазону лет (год↓, исполнитель↑)")
    print("0. Выход")

def get_user_choice():
    """Получение выбора пользователя"""
    while True:
        try:
            choice = input("\nВыберите действие (0-3): ")
            if choice == "":
                print("Ввод не может быть пустым!")
                continue

            choice_num = int(choice)

            if 0 <= choice_num <= 3:
                return choice_num
            else:
                print("\nЧисло должно быть в диапазоне (0-3)\n")
        except ValueError:
            print("\nНеверное значение\n")