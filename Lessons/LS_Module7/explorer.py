import tkinter

from tkinter import filedialog
import os



def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='kppkp файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)



window = tkinter.Tk()
window.geometry('350x150')
window.resizable(False, False)
window.title('Проводник')  # меняем название
window.configure(bg='black')
text = tkinter.Label(window, text='Файл: ', height=5, width=50, background='pink')
text.grid(column=1, row=1)  # с помощью метода grid разделили на сетку наше окно и разместили надпись
button_select = tkinter.Button(window, width=20, height=3, text='Выберите файл', foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5)

window.mainloop()