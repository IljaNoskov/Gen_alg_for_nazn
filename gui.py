from tkinter import *
from tkinter import ttk

def gen_alg(tab):
    lbl0 = Label(tab, text='Введите параметры генетического алгоритма')
    lbl0.grid(column=0, row=1)

window = Tk()
window.title("Выбирите способ генерации матрицы")
window.geometry('400x250')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

lbl0 = Label(window, text='Введите параметры генетического алгоритма')
lbl0.grid(column=0, row=0)

#
tab_control.add(tab1, text='Случайная по размерам')
lbl1 = Label(tab1, text='Введите размер квадратной матрицы')
lbl1.grid(column=0, row=0)
mat_size = Entry(tab1, width=10)
mat_size.grid(column=1, row=0)

#
tab_control.add(tab2, text='Из файла')
lbl2 = Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)
gen_alg(tab2)


#
tab_control.add(tab3, text='Задать вручную')
lbl3 = Label(tab3, text='Вкладка 3')

lbl3.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
window.mainloop()
