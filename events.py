# from tkinter import *
#
# def button_click():
#     print("Button clicked!")
#
# window =Tk()
# window.title("Button Click Example")
#
# button =Button(window, text="Click me", command=button_click)
# button.pack()
#
# window.mainloop()

# import tkinter as tk
#
# def key_press(event):
#     print("Key pressed:", event.char)
#
# def key_release(event):
#     print("Key released:", event.char)
#
# window = tk.Tk()
# window.title("KeyPress/KeyRelease Example")
#
# window.bind("<KeyPress>", key_press)
# window.bind("<KeyRelease>", key_release)
#
# window.mainloop()

# from tkinter import *
#
# def mouse_click(event):
#     print("Mouse clicked at ({}, {})".format(event.x, event.y))
#
# window =Tk()
# window.title("Mouse Click Example")
#
# window.bind("<Button-1>", mouse_click)
#
# window.mainloop()

# from tkinter import *
#
# def mouse_motion(event):
#     print("Mouse moved to ({}, {})".format(event.x, event.y))
#
# window = Tk()
# window.title("Mouse Motion Example")
#
# window.bind("<Motion>", mouse_motion)
#
# window.mainloop()

# from tkinter import *
#
# def focus_in(event):
#     print("Focus In")
#
# def focus_out(event):
#     print("Focus Out")
#
# window = Tk()
# window.title("Focus In/Focus Out Example")
#
# entry = Entry(window)
# entry.pack()
#
# entry.bind("<FocusIn>", focus_in)
# entry.bind("<FocusOut>", focus_out)
#
# window.mainloop()

# from tkinter import *
#
# def menu_selected():
#     print("Menu item selected")
#
# window = Tk()
# window.title("Menu Selection Example")
#
# menubar = Menu(window)
# file_menu = Menu(menubar, tearoff=0)
# file_menu.add_command(label="Open", command=menu_selected)
# file_menu.add_command(label="Save", command=menu_selected)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=window.quit)
# menubar.add_cascade(label="File", menu=file_menu)
#
# window.config(menu=menubar)
#
# window.mainloop()

# from tkinter import *
#
# def listbox_select(event):
#     selected_item = listbox.get(listbox.curselection())
#     print("Selected item:", selected_item)
#
# window = Tk()
# window.title("Listbox Selection Example")
#
# listbox = Listbox(window)
# listbox.pack()
#
# listbox.insert(1, "Item 1")
# listbox.insert(2, "Item 2")
# listbox.insert(3, "Item 3")
#
# listbox.bind("<<ListboxSelect>>", listbox_select)
#
# window.mainloop()

