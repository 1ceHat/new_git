team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score2+score1
time_total = team1_time+team2_time
time_avg = round(time_total/tasks_total, 3)

# Использование %
string1 = 'В команде Мастера кода участников: %d' % team1_num
string2 = 'Итого сегодня в командах участников: %d и %d' % (team1_num, team2_num)
print(string1+'\n'+string2)

# Использование format()
string1 = "Команда Волшебники данных решила задач: {score2}!".format(score2=score2)
string2 = "Волшебники данных решили задачи за {time2} с".format(time2=team2_time)
print(string1+'\n'+string2)

# Использование f-строк
if score1 > score2:
    challenge_result = 'команда Мастера кода!'
elif score1 < score2:
    challenge_result = 'команда Волшебники Данных!'
else:
    challenge_result = 'НИЧЬЯ!'
string1 = f'Команды решили {score1} и {score2}'
string2 = f'Результат битвы: победила {challenge_result}'

print(string1+'\n'+string2)

string1 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(string1)
