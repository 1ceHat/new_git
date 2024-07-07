def print_params(a=1, b='stroka', c=True):
    print(a, b, c)



print_params(b=25)
print_params(c=[1,2,3])

values_list = ['myau', True, 1.24]
values_dict = {'a': 'myau2', 'b': False, 'c': 1.54}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [20.1, 1]

print_params(*values_list_2, 42)

