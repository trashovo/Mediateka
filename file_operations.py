def read_database():
    """Чтение базы данных из файла"""

    filename = "database.txt"
    database = []
    try:
        with open(filename, 'r') as file:
            if len(file.read()) == 0:
                print('База данных пуста, добавьте записи')
                return database
            file.seek(0)
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                parts = line.split(';')
                if len(parts) != 6:
                    print(f"\nСтрока {line_num} имеет неверный формат и будет пропущена\n")
                    continue

                try:
                    track = [
                        parts[0].strip(),
                        parts[1].strip(),
                        parts[2].strip(),
                        int(parts[3]),
                        int(parts[4]),
                        int(parts[5])
                    ]
                    if int(parts[3]) <= 0 or int(parts[4]) <= 0 or int(parts[5]) <= 0:
                        print(f"\nСтрока {line_num} имеет некорректные данные и будет пропущена\n")
                        continue
                    database.append(track)
                except ValueError:
                    print(f"\nСтрока {line_num} имеет некорректные данные и будет пропущена\n")
        if len(database) > 0:
            print(f'Всего записей {len(database)}')
        if len(database) == 0:
            print('Нету верных записей в базе данных, добавьте верные данные')
        return database

    except FileNotFoundError:
        print(f"\nФайл '{filename}' не найден, начните добавлять данные, что бы создать файл")
        return database
def save_changes(database):
    filename = "database.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('#данные хранятся в формате: исполнитель;песня;альбом;год выпуска;время в секундах;кол-во прослушиваний\n')
        for track in database:
            line = ";".join(str(item) for item in track)
            file.write(line + "\n")

def add_track(database):
    """Добавление новой аудиозаписи"""
    print("\n" + "=" * 50)
    print("ДОБАВЛЕНИЕ НОВОЙ АУДИОЗАПИСИ")
    print("=" * 50)

    artist = None
    while artist is None:
        artist_input = input("Исполнитель: ").strip()
        if not artist_input:
            print("Исполнитель не может быть пустым")
        else:
            artist = artist_input

    title = None
    while title is None:
        title_input = input("Название трека: ").strip()
        if not title_input:
            print("Название трека не может быть пустым")
        else:
            title = title_input

    album = None
    while album is None:
        album_input = input("Альбом: ").strip()
        if not album_input:
            print("Альбом не может быть пустым")
        else:
            album = album_input

    year = None
    while year is None:
        try:
            year_input = int(input("Год выпуска: "))
            if year_input <= 0:
                print("Год должен быть положительным числом")
            else:
                year = year_input
        except ValueError:
            print("Неверное значение")

    duration = None
    while duration is None:
        try:
            duration_input = int(input("Длительность в секундах: "))
            if duration_input <= 0:
                print("Длительность должна быть положительным числом")
            else:
                duration = duration_input
        except ValueError:
            print("Неверное значение")

    plays = None
    while plays is None:
        try:
            plays_input = int(input("Количество прослушиваний: "))
            if plays_input < 0:
                print("Количество прослушиваний не может быть отрицательным")
            else:
                plays = plays_input
        except ValueError:
            print("Неверное значение")

    new_track = [artist, title, album, year, duration, plays]
    database.append(new_track)
    save_changes(database)
    print("\nЗапись добавлена\n")

    return database


def delete_track(database):
    """Удаление аудиозаписи"""
    if len(database) == 0:
        print("\nНету записей для удаления\n")
        return database
    print("\n" + "=" * 50)
    print("УДАЛЕНИЕ АУДИОЗАПИСИ")
    print("=" * 50)

    for i, track in enumerate(database, 1):
        print(f"{i:3d}. {track[0]} - {track[1]}, Альбом: {track[2]} ({track[3]}) Длительность в секундах: {track[4]}, Прослушиваний {track[5]}")
    while True:
        try:
            choice = int(input(f"\nВведите номер записи для удаления (1-{len(database)} или 0 для отмены): "))

            if choice == 0:
                print("\nОтмена удаления\n")
                return database

            if 1 <= choice <= len(database):
                del database[choice - 1]
                save_changes(database)
                print("\nЗапись удалена\n")
                return database
            else:
                print("\nНеверный номер записи")

        except ValueError:
            print("\nВведите число")


def edit_track(database):
    """Редактирование существующей аудиозаписи"""
    if len(database) == 0:
        print("\nНету записей для редактирования\n")
        return database
    print("\n" + "=" * 50)
    print("РЕДАКТИРОВАНИЕ АУДИОЗАПИСИ")
    print("=" * 50)

    for i, track in enumerate(database, 1):
        print(f"{i:3d}. {track[0]} - {track[1]}, Альбом: {track[2]} ({track[3]}) Длительность в секундах: {track[4]}, Прослушиваний {track[5]}")
    while True:
        try:
            choice = int(input(f"\nВведите номер записи для редактирования (1-{len(database)} или 0 для отмены): "))

            if choice == 0:
                print("\nОтмена редактирования\n")
                return database

            if 1 <= choice <= len(database):
                track_to_edit = database[choice - 1]

                print(f"\nРедактирование записи:")
                print(f"Текущие значения:")
                print(f"Исполнитель: {track_to_edit[0]}")
                print(f"Название трека: {track_to_edit[1]}")
                print(f"Альбом: {track_to_edit[2]}")
                print(f"Год выпуска: {track_to_edit[3]}")
                print(f"Длительность (сек): {track_to_edit[4]}")
                print(f"Прослушиваний: {track_to_edit[5]}")

                print("\nВведите новые значения (оставьте пустым, чтобы не менять):")

                new_artist = input(f"Исполнитель [{track_to_edit[0]}]: ").strip()
                new_title = input(f"Название трека [{track_to_edit[1]}]: ").strip()
                new_album = input(f"Альбом [{track_to_edit[2]}]: ").strip()

                check = False
                while check is False:
                    new_year = input(f"Год выпуска [{track_to_edit[3]}]: ").strip()
                    if not new_year:
                        new_year_old = 1
                        check = True
                        continue
                    try:
                        new_year = int(new_year)
                        if new_year <= 0:
                            print("Год должен быть положительным числом")
                            continue
                        new_year_old = 0
                        check = True
                    except ValueError:
                        print("Неверное значение")

                check = False
                while check is False:
                    new_duration = input(f"Длительность (сек) [{track_to_edit[4]}]: ").strip()
                    if not new_duration:
                        new_duration_old = 1
                        check = True
                        continue
                    try:
                        new_duration = int(new_duration)
                        if new_duration <= 0:
                            print("Длительность должна быть положительным числом")
                            continue
                        new_duration_old = 0
                        check = True
                    except ValueError:
                        print("Неверное значение")

                check = False
                while check is False:
                    new_plays = input(f"Прослушиваний [{track_to_edit[5]}]: ").strip()
                    if not new_plays:
                        new_plays_old = 1
                        check = True
                        continue
                    try:
                        new_plays = int(new_plays)
                        if new_plays <= 0:
                            print("Прослушиваний должно быть больше 0")
                            continue
                        new_plays_old = 0
                        check = True
                    except ValueError:
                        print("Неверное значение")

                if new_artist:
                    track_to_edit[0] = new_artist
                if new_title:
                    track_to_edit[1] = new_title
                if new_album:
                    track_to_edit[2] = new_album
                if new_year_old == 0:
                    track_to_edit[3] = new_year
                if new_duration_old == 0:
                    track_to_edit[4] = new_duration
                if new_plays_old == 0:
                    track_to_edit[5] = new_plays

                save_changes(database)
                print("\nЗапись успешно отредактирована\n")
                return database
            else:
                print("\nНеверный номер записи")

        except ValueError:
            print("\nНеверное значение")
