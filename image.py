from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
window=Tk()
# image_path="img_3.png"
# image=PhotoImage(file=image_path)
# label=Label(window,image=image)
# label.pack()

image_path="img_1.png"
image=Image.open(image_path)
image_tk=ImageTk.PhotoImage(image)
label=Label(window,image=image_tk)
label.pack()
window.mainloop()