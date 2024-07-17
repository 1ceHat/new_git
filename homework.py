first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(x)-len(y) for x, y in zip(first, second) if len(x) != len(y))

max_len = max(len(first), len(second))
second_result = (len(first[x]) == len(second[x]) for x in range(max_len))

print(list(first_result))
print(list(second_result))
