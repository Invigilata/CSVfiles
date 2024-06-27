import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    wanted_cities = set()

    with open('travel-notes.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, visited, wanted = row[0], row[1], row[2]
            if name.startswith(first_letter):
                visited_cities.update(visited.split(';'))
                wanted_cities.update(wanted.split(';'))

    # Города, в которых не были
    never_visited_cities = wanted_cities - visited_cities
    # Сортировка городов в алфавитном порядке
    visited_cities = sorted(visited_cities)
    wanted_cities = sorted(wanted_cities)
    never_visited_cities = sorted(never_visited_cities)

    first_city_to_visit = never_visited_cities[0] if never_visited_cities else None

    with open('holiday.csv', mode='w', encoding='utf-8') as file:
        file.write(f"Have visited: {', '.join(visited_cities)}\n")
        file.write(f"Want to visit: {', '.join(wanted_cities)}\n")
        file.write(f"No one has been to: {', '.join(never_visited_cities)}\n")
        if first_city_to_visit:
            file.write(f"In the end, we will go to: {first_city_to_visit}\n")

# Вызова функции
write_holiday_cities('G')
