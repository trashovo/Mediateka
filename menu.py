def display_main_menu():
    """Отображение главного меню"""

    print("1. Все аудиозаписи (исполнитель↑, год↓, прослушивания↓)")
    print("2. Записи конкретного исполнителя (альбом↓, название↑)")
    print("3. Записи по диапазону лет (год↓, исполнитель↑)")
    print("Редактирование базы данных:")
    print("4. Добавить новую запись")
    print("5. Редактировать запись")
    print("6. Удалить запись")
    print("0. Выход")

def get_user_choice():
    """Получение выбора пользователя"""
    while True:
        try:
            choice = int(input("\nВыберите действие (0-6): "))
            if 0 <= choice <= 6:
                return choice
            else:
                print("\nЧисло должно быть в диапазоне (0-3)\n")
        except ValueError:
            print("\nНеверное значение")

def choice_database():
    print("Выберите базу данных:")
    print("1. Использовать готовую базу данных")
    print("2. Создать новую пустую базу данных для теста")
    while True:
        try:
            choice_d = int(input("Ваш выбор (1-2): "))
            if choice_d >= 1 and choice_d <= 2:
                return choice_d
            else:
                print("Введите 1 или 2")
        except ValueError:
            print("\n Неверное значение\n")
