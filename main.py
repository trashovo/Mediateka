from file_operations import read_database
from reports import report_all_tracks_sorted, report_artist_tracks, report_tracks_by_year_range
from menu import display_main_menu, get_user_choice


database = read_database()

if not database:
    exit()

print("=" * 60)
print("МЕДИАТЕКА")
print("=" * 60)

while True:
    display_main_menu()
    choice = get_user_choice()

    if choice == 1:
        report_all_tracks_sorted(database)

    elif choice == 2:
        report_artist_tracks(database)

    elif choice == 3:
        report_tracks_by_year_range(database)

    elif choice == 0:
        print("\nВыход из программы")
        break
