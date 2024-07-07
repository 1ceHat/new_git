def calculate_structure_sum(data_structer):
    if isinstance(data_structer, list) or isinstance(data_structer, tuple) or isinstance(data_structer, set):
        sum_len = 0
        for value in data_structer:
            sum_len += calculate_structure_sum(value)
        return sum_len
    elif isinstance(data_structer, dict):
        sum_len = 0
        for key, value in data_structer.items():
            len_key = calculate_structure_sum(key)
            len_value = calculate_structure_sum(value)
            sum_len += len_value+len_key
        return sum_len
    elif isinstance(data_structer, str):
        return len(data_structer)
    elif isinstance(data_structer, int) or isinstance(data_structer, float):
        return data_structer



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_len = calculate_structure_sum(data_structure)
print(sum_len)