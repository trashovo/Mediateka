def read_database():
    """Чтение базы данных из файла"""
    database = []
    filename= "database.txt"

    try:
        with open(filename, 'r') as file:
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
            print('Нету верных записей в базе данных')
        return database

    except FileNotFoundError:
        print(f"\nОшибка: файл '{filename}' не найден")
        return None