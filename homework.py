def write_holiday_cities(first_letter):
    visited_cities = []
    wish_visit = []

    with open('travel-notes.csv') as file:
        for line in file:
            line = line.replace('\n', '')
            person, visited, wish = line.split(',')

            if person.lower()[0] == first_letter.lower():
                for city in visited.split(';'):
                    if city is not None and city not in visited_cities:
                        visited_cities.append(city)

                for city in wish.split(';'):
                    if city is not None and city not in wish_visit:
                        wish_visit.append(city)

    visited_cities.sort()
    wish_visit.sort()
    never_visited = [x for x in wish_visit if x not in visited_cities]

    with open('holiday.csv', 'w', encoding='utf-8') as file:
        count = 0
        for list_ in [visited_cities, wish_visit, never_visited]:
            if count == 0:
                string = 'Посещенные города: ,'
            elif count == 1:
                string = 'Хотят посетить: ,'
            elif count == 2:
                string = 'Никогда не посещали: ,'
            count += 1

            for city in list_:
                string += city + ';'
            if string[-1] == ';':
                string = string[:-1]
            print(string)
            file.write(string+'\n')
        print(f'Следующим городом будет: {wish_visit[0]}')
        file.write(f'Следующим городом будет: ,{wish_visit[0]}')


write_holiday_cities('L')
