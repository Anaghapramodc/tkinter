from tkinter import *

window = Tk()
window.title("basic_app")
window.geometry("600x400")
window.resizable(False, False)
window.iconbitmap("./images.ico")

def sum():
    s = int(n1.get()) + int(n2.get())
    print(s)
    result.set(s)

def diff():
    s = int(n1.get()) - int(n2.get())
    print(s)
    result.set(s)

def multi():
    s = int(n1.get()) * int(n2.get())
    print(s)
    result.set(s)

def div():
    s = int(n1.get()) / int(n2.get())
    print(s)
    result.set(s)

result = StringVar()

lb1 = Label(window, text="number 1: ")
lb2 = Label(window, text="number 2: ")
lb3 = Label(window, text="Result: ")
n1 = Entry(window)
n2 = Entry(window)
n3 = Entry(window, textvariable=result)

lb1.pack()
n1.pack()
lb2.pack()
n2.pack()
lb3.pack()
n3.pack()

button_frame = Frame(window)
button_frame.pack()

btn1 = Button(button_frame, text="+", command=sum)
btn1.pack(side="left", padx=10, pady=10)
btn2 = Button(button_frame, text="-", command=diff)
btn2.pack(side="left", padx=10, pady=10)
btn3 = Button(button_frame, text="*", command=multi)
btn3.pack(side="left", padx=10, pady=10)
btn4 = Button(button_frame, text="/", command=div)
btn4.pack(side="left", padx=10, pady=10)

window.mainloop()

