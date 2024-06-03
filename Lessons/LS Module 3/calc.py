import tkinter as tk

window = tk.Tk()  # создаем окно
window.title('Калькулятор')  # меняем название
window.geometry('350x450')  # меняем размер окна
window.resizable(False, False)
button_plus = tk.Button(window, text='+', width=2, height=2)  # добавили кнопку
button_plus.place(x=100, y=300)  # разместили кнопку
button_minus = tk.Button(window, text='-', width=2, height=2)
button_minus.place(x=150, y=300)
button_mult = tk.Button(window, text='*', width=2, height=2)
button_mult.place(x=200, y=300)
button_dev = tk.Button(window, text='/', width=2, height=2)
button_dev.place(x=250, y=300)
number1_entry = tk.Entry(window, width=28)  # размещаем поле для ввода
number1_entry.place(x=100, y=100)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=200)
number1 = tk.Label(window, text=' Введите первое число ')
number1.place(x=100, y=75)
number2 = tk.Label(window, text=' Введите второе число ')
number2.place(x=100, y=125)
answer_entry = tk.Label(window, text=' НА НАХУЙ ОТВЕТ ')
answer_entry.place(x=100, y=175)
window.mainloop()