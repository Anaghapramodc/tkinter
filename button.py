# from tkinter import *
#
# def on_checkbox_toggle():
#     # This function will be called when the Checkbutton is toggled
#     if check_var.get():
#         label.config(text="Checkbox is checked")
#     else:
#         label.config(text="Checkbox is unchecked")
#
# # Create the main window
# window =Tk()
# window.title("Checkbutton Example")
#
# # Create a Tkinter variable to hold the state of the Checkbutton
# check_var =BooleanVar()
#
# # Create a Checkbutton widget
# check_button = Checkbutton(window, text="Check me", variable=check_var, command=on_checkbox_toggle)
#
# # Place the Checkbutton in the window
# check_button.pack(pady=10)
#
# # Create a label to display the status of the Checkbutton
# label = Label(window, text="")
# label.pack()
#
# # Run the Tkinter event loop
# window.mainloop()

# from tkinter import *
#
# def show_selection():
#     # Display the selected option in the console
#     print("Selected option:", var.get())
#
# # Create the main window
# window =Tk()
# window.title("Radio Button Example")
#
# # Variable to hold the selected option
# var = StringVar()
#
# # Create radio buttons
# option1 = Radiobutton(window, text="Option 1", variable=var, value="Option 1")
# option2 = Radiobutton(window, text="Option 2", variable=var, value="Option 2")
# option3 = Radiobutton(window, text="Option 3", variable=var, value="Option 3")
#
# # Position radio buttons using grid layout
# option1.grid(row=0, column=0, sticky="w")
# option2.grid(row=0, column=1, sticky="w")
# option3.grid(row=0, column=2, sticky="w")
#
# # Button to display selected option
# show_button = Button(window, text="Show Selection", command=show_selection)
# show_button.grid(row=3, column=0, pady=10)
#
# # Start the Tkinter event loop
# window.mainloop()

#
# from tkinter import *
# from tkinter.ttk import Combobox
# #
# # Create the main window
# window = Tk()
# window.geometry("300x200")
# window.title("Combo Box Example")
#
# # Define a list of options
# options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
#
# # Create a StringVar to store the selected option
# selected_option = StringVar()
#
# # Create the combo box and assign options to it
# combo_box = Combobox(window, textvariable=selected_option, values=options)
# combo_box.pack(pady=20)
#
# # Set a default value
# combo_box.set("Select an option")
#
# # Function to get the selected option
# def get_selected_option():
#     print("Selected Option:", selected_option.get())
#
# # Button to get the selected option
# btn = Button(window, text="Get Selected Option", command=get_selected_option)
# btn.pack()
import tkinter as tk
from tkinter import messagebox

def show_message_box():
    messagebox.showinfo("Message", "This is a message box!")

root = tk.Tk()

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button to show the message box
button = tk.Button(root, text="Show Message Box", command=show_message_box)
button.pack()

root.mainloop()

# Run the Tkinter event loop
window.mainloop()


