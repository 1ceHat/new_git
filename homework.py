import random as rnd

students = {'John', 'Doe', 'Sonic', 'Star', 'Uaou', 'Aaaa'}
sorted_students = sorted(tuple(students))
grades = []
average_marks = {}

for student in sorted_students:
    grades.append([])
    for i in range(rnd.randint(2,10)):
        grades[-1].append(rnd.randint(2,5))
    print(grades[-1])
    average_marks[student] = round(sum(grades[-1])/len(grades[-1]), 2)


for key, value in average_marks.items():
    print(f"{key}'s average mark is {value}")