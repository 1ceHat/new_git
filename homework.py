import json
from operator import itemgetter


def employees_rewrite(sort_type):
    data = ''
    try:
        with open('employees.json') as file:
            data = json.load(file)
            sorted_json = sorted(data['employees'], key=itemgetter(sort_type))
            data['employees'] = sorted_json
    except:
        raise ValueError('Bad key for sorting')

    with open(f'employees_{sort_type}_sorted.json', 'w') as file:
        json.dump(data, file)


employees_rewrite('salary')
