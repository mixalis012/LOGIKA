from customtkinter import*
from random import randint
window = CTk()
window.geometry('400x400')#CTk
def btn_position():
    x_rand = randint(0, window.winfo_width()-btn_no.winfo_width())
    y_rand = randint(0, window.winfo_height()-btn_no.winfo_height())
    btn_no.place(x=x_rand, y=y_rand)
def show_win():
    window2 = CTk()
    window2.geometry('200x100')
    label_win = CTkLabel(window2, text='Cool!')
    label_win.pack(pady=20)

    window2.mainloop()
label = CTkLabel(window, text='your name mixalis?')
label.pack(pady=40)
btn_no = CTkButton(window, text='no', command=btn_position)
btn_no.place(x=50, y=200)
btn_yes = CTkButton(window, text='yes', command=show_win)
btn_yes.place(x=200, y=200)
window.mainloop()
