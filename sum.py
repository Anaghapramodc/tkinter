from tkinter import *
window= Tk()
window.title("basic_app")#to give title to the windo
window.geometry("600x400")#used to fix the length and hight of the window
window.resizable(False,False)#used to remove the resizeing option of the window
window.iconbitmap("./images.ico")#used to change icon

def sum():
    s=int(n1.get())+int(n2.get())
    print(s)
    result.set(s)
result=StringVar()


lb1=Label(window,text="number 1: ")
lb2=Label(window,text="number 2: ")
lb3=Label(window,text="Result: ")
n1=Entry(window)
n2=Entry(window)
n3=Entry(window,textvariable=result)

lb1.pack()
n1.pack()
lb2.pack()
n2.pack()
lb3.pack()
n3.pack()

btn=Button(window,text="submit",command=sum)
btn.pack()


window.mainloop()#to read the window