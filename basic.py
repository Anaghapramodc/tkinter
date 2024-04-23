
from tkinter import *
window= Tk()
window.title("basic_app")#to give title to the windo
window.geometry("400x600")#used to fix the length and hight of the window
# window.resizable(False,False)#used to remove the resizeing option of the window
# window.resizable(True,False)
# window.resizable(False,True)
window.iconbitmap("./images.ico")#used to change icon
# window.configure(bg="black")#used to change background colour
# window.attributes("-alpha",1)#used to transperand baground
# window.attributes("-topmost",1)#used to fix the tab always in the top window


#add text box
def get_text():
    print(text.get("1.0", "end-1c"))
    name = text.get("1.0", "end-1c")  # Retrieve all text from start to end
    lb2.config(text=f"hello {name}")


text =Text(window)
text.pack()
button = Button(window, text="Get Text", command=get_text)
button.pack()
lb2 = Label(window, text="")
lb2.pack()



#
# canvas =Canvas(window, width=200, height=500)
# canvas.pack()
# canvas.create_rectangle(50, 200, 150, 300, fill="blue")


# Draw a blue rectangle on the canvas
# Coordinates (50, 200) represent the top-left corner of the rectangle
# Coordinates (150, 300) represent the bottom-right corner of the rectangle


# Calculate the coordinates to place the canvas in the middle of the window
# canvas_width = 200
# canvas_height = 500
# window.update_idletasks()  # Update the window to get its size
# window_width = window.winfo_width()  # Get the width of the window
# window_height = window.winfo_height()  # Get the height of the window
# x = (window_width - canvas_width) / 2  # Calculate the x coordinate for centering horizontally
# y = (window_height - canvas_height) / 2  # Calculate the y coordinate for centering vertically
#
# # Place the canvas in the middle of the window
# canvas.place(x=x, y=y)

# Create a Frame
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
#how to add labels ,symbols button in tkinter
# lb1=Label(window, text="enter your name")
# lb1.pack()#used to add a labal to the window
#
# t1=Entry(window)
# t1.pack()#used to create a text box
#
# def message():
#     name=t1.get()
#     lb2=Label(window,text=f"Hello {name}")
#     lb2.pack()
#
#
# btn1=Button(window,text="click",command=message)
# btn1.pack()# used to add button



window.mainloop()#to read the window