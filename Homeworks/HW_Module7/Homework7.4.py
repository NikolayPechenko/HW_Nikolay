name1 = 'Мастера кода'
name2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.51
team2_time = 2153.31
tasks_total = score1 + score2
time_avg = round((team1_time + team2_time) / tasks_total, 2)

if score1 > score2 or score1 == score2 and team2_time > team1_time:
    challenge_result = f'Победа команды {name1}'
elif score1 < score2 or score1 == score2 and team2_time < team1_time:
    challenge_result = f'Победа команды {name2}'
else:
    challenge_result = 'Ничья'

print('В команде Мастера кода участников: %d !' % team1_num)
print('Итого сегодня в командах участников: %s и %d !' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

