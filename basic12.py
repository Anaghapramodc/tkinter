from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
window=Tk()
window.title("python")
window.geometry("600x400")
# window.resizable(False,False)
# window.resizable(True,False)
# window.resizable(False,True)
window.iconbitmap("./images.ico")
# window.configure(bg="#f42541")
# window.attributes("-alpha",0.5)
# window.attributes("-topmost",1)

# lb1=Label(window,text="Leran python")
# lb1.pack()
# t1=Entry(window)
# t1.pack()
# btn=Button(window,text="submit")
# btn.pack()




# def message():
#     lb=Label(window,text="Hello World !!!!")
#     lb.pack()
#
# btn=Button(window,text="submit",command=message)
#
# btn.pack()

#bknd
# def message():
#     name=t.get()
#     lb=Label(window,text=f"Hello  {name}")
#     lb.pack()
#
# #frndnt
# lb=Label(window,text="enter your name")
# lb.pack()
# t=Entry(window)
# t.pack()
# btn=Button(window,text="submit",command=message)
# btn.pack()


# result=StringVar()
# def sum():
#     sum=int(t1.get())+int(t2.get())
#     print(sum)
#     result.set(sum)
#
# lb1=Label(window,text="1st number")
# lb1.pack()
# t1=Entry(window)
# t1.pack()
# lb2=Label(window,text="2st number")
# lb2.pack()
# t2=Entry(window)
# t2.pack()
# lb3=Label(window,text="Result :")
# lb3.pack()
# t3=Entry(window,textvariable=result)
# t3.pack()
# btn=Button(window,text="submit",command=sum)
# btn.pack()
#

#text box
# def get_text():
#     v=text.get("1.0","end-1c")
#     lb2.config(text=f"{v}")
# text=Text(window)
# text.pack()
# button=Button(window,text="get text",command=get_text)
# button.pack()
# lb2=Label(window,text="")
# lb2.pack()



#canvas
# canvas=Canvas(window,width=1000,height=1000)
# canvas.pack()
# canvas.create_rectangle(0,0,1000,1000,fill="blue")

# frame
# frame=Frame(window)
# frame.pack(padx=100,pady=150)
#
#
# #list box
# listbox=Listbox(frame,selectmode=MULTIPLE)
# for i in range(1,21):
#      listbox.insert(END,f"list{i}")
# listbox.pack(side=LEFT,fill=BOTH,expand=True)
#
# #scroller
# def scroll(*args):
#     listbox.yview(*args)
#
# sc=Scrollbar(frame,command=scroll)
# sc.pack(side=RIGHT,fill=Y)
#
# listbox.config(yscrollcommand=sc.set)
#
#
#
# #bind
# def select(event):
#     s=listbox.curselection()
#     for i in s:
#       print("select:",listbox.get(i))
# listbox.bind("<<ListboxSelect>>",select)
#
# def menu_select():
#     w = Tk()
#     w.title("python")
#     w.geometry("600x400")
#     w.mainloop()
#
# m=Menu(window)
# window.config(menu=m)
# file_menu=Menu(m,tearoff=0)
# m.add_cascade(label="File",menu=file_menu)
# file_menu.add_command(label="New",command=menu_select)
# file_menu.add_command(label="open")
# file_menu.add_separator()
# file_menu.add_command(label="exit",command=window.quit)
#
# edit_menu=Menu(m,tearoff=0)
# m.add_cascade(label="Edit",menu=edit_menu)
# edit_menu.add_command(label="cut")
# edit_menu.add_command(label="copy")
# edit_menu.add_command(label="past")
#
#
#
#
#
#
# def key_press(event):
#     print("key pressed:",event.char)
#
# def key_release(event):
#     print("key release:",event.char)
#
#
# window.bind("<KeyPress>",key_press)
# window.bind("<KeyRelease>",key_release)
#
#
#
# def checkbox():
#     if check_var.get():
#         l.config(text="check box is checked")
#     else:
#         l.config(text="check box is not checked")
# check_var=BooleanVar()
# c=Checkbutton(window,text="check me",variable=check_var,command=checkbox)
# c.pack(pady=10)
# l=Label(window,text="")
# l.pack()

#
# def show_selection():
#     print("selected option:",var.get())
# var=StringVar()
# o1=Radiobutton(window,text="option1",variable=var,value="option1")
# o2=Radiobutton(window,text="option2",variable=var,value="option2")
# o3=Radiobutton(window,text="option3",variable=var,value="option3")
#
# o1.grid(row=0,column=0)
# o2.grid(row=0,column=1)
# o3.grid(row=0,column=2)
#
# show=Button(window,text="show selection",command=show_selection)
# show.grid(row=1,column=0)
#


#
# def select():
#     print("select item:",var.get())
#
# option=["option1","option2","option3","option4"]
# var=StringVar()
# c=Combobox(window,textvariable=var,values=option)
# c.pack()
# c.set("select an option")
# btn=Button(window,text="select option",command=select)
# btn.pack()



def shomsg():
    messagebox.showinfo("successfull","this is an information message")


btn=Button(window,text="show msgbox",command=shomsg)
btn.pack()




















window.mainloop()