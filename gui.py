from tkinter import *
import gen_alg


def test():
    get_matrix = matrix_file_z.get()
    try:
        mat = gen_alg.matrix_from_file(get_matrix)
    except FileNotFoundError:
        lbl_ans["text"] = "Файл с таким именем не найден"
        return -1
    get_bool = chk_state.get()
    if get_bool:
        a = len(mat)
        pokol_num = 10*a
        pokol_size = 50*a
        child_per = 20
        mutatiom_per = 20
    else:
        pokol_num = max(1, tk_pokol_num.get())
        pokol_size = max(1, tk_pokol_size.get())
        child_per = max(1, tk_child_per.get())
        mutatiom_per = max(1, tk_mutatiom_per.get())
        if child_per + mutatiom_per > 50:
            lbl_ans["text"] = "Вы выбрали слишком большое проценты потомков или мутантов"
    rez = gen_alg.gen_alg(mat, pokol_num, pokol_size, round(pokol_size * child_per / 100),
                          round(mutatiom_per * pokol_size / 100))
    lbl_ans["text"] = f"Сумма={rez[0]}, Кодировка:{rez[1]}"


window = Tk()
window.title("Решение задачи о назначениях")
window.geometry("600x400")

tk_pokol_num = IntVar()
tk_pokol_size = IntVar()
tk_child_per = IntVar()
tk_mutatiom_per = IntVar()
matrix_file_z = StringVar()
chk_state = BooleanVar()
chk_state.set(True)


message_1 = Label(text="Введите название файла матрицы")
message_2 = Label(text="Введите количество поколений")
message_3 = Label(text="Введите размер поколения")
message_4 = Label(text="Введите % потомков")
message_5 = Label(text="Введите % мутантов")
lbl_ans = Label(text="Тут будет ответ")


ent_matrix_file = Entry(textvariable=matrix_file_z)
ent_pokol_num = Entry(textvariable=tk_pokol_num)
ent_pokol_size = Entry(textvariable=tk_pokol_size)
ent_child_per = Entry(textvariable=tk_child_per)
ent_mutatiom_per = Entry(textvariable=tk_mutatiom_per)

b = Button(command=test, text="Рассчитать")

chk = Checkbutton(window, text='Использовать стандартные значения параметров', var=chk_state)

message_1.grid(row=0, column=0)
ent_matrix_file.grid(row=0, column=1)
chk.grid(row=1, column=0)
message_2.grid(row=2, column=0)
ent_pokol_num.grid(row=2, column=1)
message_3.grid(row=3, column=0)
ent_pokol_size.grid(row=3, column=1)
message_4.grid(row=4, column=0)
ent_child_per.grid(row=4, column=1)
message_5.grid(row=5, column=0)
ent_mutatiom_per.grid(row=5, column=1)
b.grid(row=6, column=1)
lbl_ans.grid(row=7, column=0)


window.mainloop()

