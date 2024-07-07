calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string='string'):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string_info='string', list_to_search=['stri', 'strin', 'string1']):
    count_calls()
    # перевели пришедшие данные в строковый тип с нижним написанием
    for i in range(len(list_to_search)):
        list_to_search[i] = str(list_to_search[i]).lower()
    string_info = str(string_info).lower()

    if string_info in list_to_search:
        return True
    else:
        return False


list1 = ['ban', 'BaNaN', 'urBAN']
list2 = ['recycling', 'cyclic']

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', list1))
print(is_contains('cycle', list2))
print(calls)
