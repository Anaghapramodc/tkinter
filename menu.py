from tkinter import *
window= Tk()
window.title("basic_app")#to give title to the windo
window.geometry("400x600")#used to fix the length and hight of the window
# window.resizable(False,False)#used to remove the resizeing option of the window
# window.resizable(True,False)
# window.resizable(False,True)
window.iconbitmap("./images.ico")#used to change icon
frame = Frame(window)
frame.pack(pady=150)

# Create a Listbox
listbox =Listbox(frame, selectmode=MULTIPLE)
for i in range(1, 21):
    listbox.insert(END, f"Item {i}")
listbox.pack(side=LEFT, fill=BOTH, expand=True)

# Create a Scrollbar
def on_scroll(*args):
    listbox.yview(*args)
scrollbar = Scrollbar(frame, command=on_scroll)
scrollbar.pack(side=RIGHT, fill=Y)

# Link Listbox and Scrollbar
listbox.config(yscrollcommand=scrollbar.set)

# Bind event to Listbox
def on_select(event):
    selected_indices = listbox.curselection()
    for i in selected_indices:
        print("Selected:", listbox.get(i))
listbox.bind("<<ListboxSelect>>", on_select)

# Create a Menu
menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

window.mainloop()#to read the window