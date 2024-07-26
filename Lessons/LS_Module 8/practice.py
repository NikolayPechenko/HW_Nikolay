def calc(line):
    operand1, operation, operand2 = line.split(' ')
    # operand1 = line.split(' ')[0]
    # operation = line.split(' ')[1]
    # operand2 = line.split(' ')[2]
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operation == '+':
        print(f'Результат: {operand1 + operand2}')
    if operation == '-':
        print(f'Результат: {operand1 - operand2}')
    if operation == '/':
        print(f'Результат: {operand1 / operand2}')
    if operation == '%':
        print(f'Результат: {operand1 % operand2}')
    if operation == '//':
        print(f'Результат: {operand1 // operand2}')
    if operation == '//':
        print(f'Результат: {operand1 * operand2}')


with open('data.txt', 'r') as file:
    i = 0
    for line in file:
        i += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Пошел нахуй в строчке {i}, идешь нахуй потому что мало данных или даже много')
            if 'invalid' in exc.args[0]:
                print(f'Пошел нахуй в строчке {i}, идешь нахуй потому что инвалид')
