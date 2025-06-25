from customtkinter import*
from random import choice

window = CTk()
window.geometry("300x200")
window.title('Random password')
password_len = 4

def gen_pass():
    result = ''.join(choice('0123456789')for i in range(password_len))
    password_entry.delete(0, 'end')
    password_entry.insert(0, result)
def show_len_pass(value):
    global password_len
    password_len = int(value)
    lenght_label.configure(text=str(password_len))
    gen_pass()
password_entry = CTkEntry(window, width=200, justify='center')
password_entry.pack(pady=20)
btn_gen = CTkButton(window, text='Random', command=gen_pass)
btn_gen.pack(pady=5)
frame = CTkFrame(window)
frame.pack(pady=10)


lenght_label = CTkLabel(frame, text=str(password_len), width=40)
lenght_label.pack(side='left', padx=10)

len_slider = CTkSlider(frame, from_=4, to=20, command=show_len_pass)
len_slider.set(password_len)
len_slider.pack(side='left')

window.mainloop()