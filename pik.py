from customtkinter import*
from PIL import Image

window = CTk()
window.geometry('400x400')

image = Image.open('gta.webp')
img_CTk = CTkImage(light_image=image, size=(300,300))

label = CTkLabel(window, text='', image=img_CTk)
label.pack(pady=10)

window.mainloop()