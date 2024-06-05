import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())  # получаем число с визуального объекта
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):     # принимающая функция, которая в значение value принимает наш результат res, удаляет старое значение, выводит в поле для оюъекта
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)  # вставляем в поле для ответа


def add():
    num1 = int(number1_entry.get())  # получаем число с визуального объекта
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)  # вставляем в поле для ответа


def mins():
    num1, num2 = get_values()  # получаем значение из функций
    res = num1 - num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)  # вставляем в поле для ответа


def mlt():
    num1, num2 = get_values()  # получаем значение из функций
    res = num1 * num2
    insert_values(res)


def dev():
    num1, num2 = get_values()  # получаем числа с визуального объекта
    res = num1 / num2
    insert_values(res)  # вставляем в поле для ответа




window = tk.Tk()  # создаем окно
window.title('Калькулятор')  # меняем название
window.geometry('350x450')  # меняем размер окна
window.resizable(False, False)
button_plus = tk.Button(window, text='+', width=2, height=2, command=add)  # добавили кнопку, комманду, которая ссылается на функцию
button_plus.place(x=100, y=300)  # разместили кнопку
button_minus = tk.Button(window, text='-', width=2, height=2, command=mins)
button_minus.place(x=150, y=300)
button_mult = tk.Button(window, text='*', width=2, height=2, command=mlt)
button_mult.place(x=200, y=300)
button_dev = tk.Button(window, text='/', width=2, height=2, command=dev)
button_dev.place(x=250, y=300)
number1_entry = tk.Entry(window, width=28)  # размещаем поле для ввода (Entry)
number1_entry.place(x=100, y=100)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=200)
number1 = tk.Label(window, text=' Введите первое число ')  # создаем надпись (Label)
number1.place(x=100, y=75)
number2 = tk.Label(window, text=' Введите второе число ')
number2.place(x=100, y=125)
answer = tk.Label(window, text=' НА НАХУЙ ОТВЕТ ')
answer.place(x=100, y=175)
window.mainloop()
