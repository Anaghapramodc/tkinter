from tkinter import *
window= Tk()
window.title("basic_app")#to give title to the windo
window.geometry("600x600")#used to fix the length and hight of the window
window.resizable(False,False)#used to remove the resizeing option of the window
window.iconbitmap("./images.ico")#used to change icon


def message():
    name1 = n1.get()
    name2 = n2.get()
    name3 = n3.get()
    name4 = n4.get()
    name5 = n5.get()
    lb2 = Label(window, text=f"candidate name :{name1} {name2} {name3}")
    lb2.pack()
    lb3 = Label(window, text=f"Gmail :{name4}")
    lb3.pack()
    lb4 = Label(window, text=f"Mobile No :{name5}")
    lb4.pack()


lb1=Label(window,text="First name: ")
lb2=Label(window,text="middile name: ")
lb3=Label(window,text="last name: ")
lb4=Label(window,text="gmail: ")
lb5=Label(window,text="mobile no: ")
lb6=Label(window,text="password: ")
lb7=Label(window,text="conform password: ")
n1=Entry(window)
n2=Entry(window)
n3=Entry(window)
n4=Entry(window)
n5=Entry(window)
n6=Entry(window)
n7=Entry(window)
lb1.pack()
n1.pack()
lb2.pack()
n2.pack()
lb3.pack()
n3.pack()
lb4.pack()
n4.pack()
lb5.pack()
n5.pack()
lb6.pack()
n6.pack()
lb7.pack()
n7.pack()
btn=Button(window,text="submit",command=message)
btn.pack()


window.mainloop()#to read the window