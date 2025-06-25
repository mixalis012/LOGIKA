from customtkinter import*
window = CTk()
for i in range(64):
    if (i//8)%2!=0:
        if (i%8)%2!=0:
            color = 'black'
        else:
            color = 'white'
    else:
        if (i%8)%2!=0:
            color = 'white'
        else:
            color = 'black'
    CTkButton(window, fg_color=color, text='', width=40, height=40).grid(row=i//8, column=i%8, padx=5, pady=5)
window.mainloop()
