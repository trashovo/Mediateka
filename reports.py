from sorting import multi_key_sort


def format_duration(seconds):
    """Форматирование длительности из секунд в минуты:секунды"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


def display_tracks(tracks, title):
    """Отображение списка треков"""
    print(f"\n{title}\n")
    header = f"{'№':>3} {'Исполнитель':<20} {'Трек':<30} {'Альбом':<30} {'Год':>4} {'Длительность':>7} {'Прослушивания':>15}"
    print(header)
    print('-' * 120)

    for i, track in enumerate(tracks, 1):
        print(f"{i:3d}. {track[0]:<20} {track[1]:<30} {track[2]:<30} {track[3]:>4} {format_duration(track[4]):>7} {track[5]:>15}")


    print(f"\nВсего записей: {len(tracks)}\n")


def report_all_tracks_sorted(database):
    """Отчет 1: Все записи, отсортированные по исполнителю(↑), году(↓), прослушиваниям(↓)"""
    if not database:
        print('\nЗаписи отсутствуют, добавьте записи для работы\n')
        return None
    keys = [
        (lambda x: x[0], False),
        (lambda x: x[3], True),
        (lambda x: x[5], True)
    ]

    sorted_tracks = multi_key_sort(database, keys)
    display_tracks(sorted_tracks, "ОТЧЕТ 1: Все аудиозаписи")

    return sorted_tracks


def report_artist_tracks(database):
    """Отчет 2: Все записи конкретного исполнителя"""
    if not database:
        print('\nЗаписи отсутствуют, добавьте записи для работы\n')
        return None

    artists = {}
    for track in database:
        artist = track[0]
        if artist not in artists:
            artists[artist] = 0
        artists[artist] += 1
    sorted_artists = sorted(artists.items())

    print("\n" + "=" * 50)
    print("Список исполнителей:")
    print("=" * 50)

    for i, (artist, count) in enumerate(sorted_artists, 1):
        print(f"{i:3d}. {artist:<25} ({count} записей)")

    while True:
        try:
            choice = int(input("\nВведите номер исполнителя (0 для отмены): "))

            if choice == 0:
                return []

            if choice < 1 or choice > len(sorted_artists):
                print("Неверный номер исполнителя")
                continue
            else:
                break

        except ValueError:
            print("Неверное значение")
            continue

    selected_artist = sorted_artists[choice - 1][0]

    artist_tracks = [track for track in database if track[0] == selected_artist]

    keys = [
        (lambda x: x[2], True),
        (lambda x: x[1], False)
    ]

    sorted_tracks = multi_key_sort(artist_tracks, keys)
    display_tracks(sorted_tracks, f"ОТЧЕТ 2: Аудиозаписи исполнителя '{selected_artist}'")

    return sorted_tracks


def report_tracks_by_year_range(database):
    """Отчет 3: Записи в диапазоне лет"""
    if not database:
        print('\nЗаписи отсутствуют, добавьте записи для работы\n')
        return None

    years = [track[3] for track in database]
    min_year = min(years)
    max_year = max(years)

    print(f"\nДоступный диапазон лет: {min_year} - {max_year}")

    while True:
        try:
            n1 = int(input("\nВведите начальный год (0 для отмены): "))

            if n1 == 0:
                return []

            if n1 < min_year or n1 > max_year:
                print(f"\nГод должен быть в диапазоне {min_year}-{max_year}")
                continue
            else:
                break

        except ValueError:
            print("\nНеверное значение")
            continue
    if n1 == max_year:
        n2 = n1
        print(f'\nНачальный год равен максимальному, поиск за {n1} год')
    else:
        while True:
                try:
                    n2 = int(input("Введите конечный год: "))

                    if n2 < n1 or n2 > max_year:
                        print(f"\nКонечный год должен быть в диапазоне {n1}-{max_year}\n")
                        continue
                    else:
                        break

                except ValueError:
                    print("\nНеверное значение\n")
                    continue

    filtered_tracks = [track for track in database if n1 <= track[3] <= n2]

    if not filtered_tracks:
        print(f"\nВ период {n1}-{n2} записей не найдено\n")
        return []

    keys = [
        (lambda x: x[3], True),
        (lambda x: x[0], False)
    ]

    sorted_tracks = multi_key_sort(filtered_tracks, keys)
    if n1 != n2:
        display_tracks(sorted_tracks, f"ОТЧЕТ 3: Аудиозаписи за период {n1}-{n2}")
    else:
        display_tracks(sorted_tracks, f"ОТЧЕТ 3: Аудиозаписи за {n1} год")

    return sorted_tracks
