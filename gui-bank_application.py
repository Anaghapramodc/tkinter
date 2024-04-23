import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class BankApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Application")
        self.master.geometry("1000x650")
        self.master.resizable(False, False)
        # Background image
        self.background_image = PhotoImage(file="img_6.png")
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.iconbitmap("img_7.png")

        # Dummy user data
        self.users = {"user1": {"password": "password123", "balance": 1000},
                      "user2": {"password": "password456", "balance": 2000}}

        self.logged_in_user = None

        self.create_menu()
        self.home()

    def home(self):
        self.image_path = "img_6.png"
        self.image = PhotoImage(file=self.image_path)

        # Create a label and display the image
        self.label = tk.Label(self.master, image=self.image)
        self.label.pack()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        user_menu = tk.Menu(menu, tearoff=False)
        user_menu.add_command(label="Login", command=self.create_login_screen)
        user_menu.add_command(label="Register", command=self.create_register_screen)
        user_menu.add_separator()
        user_menu.add_command(label="Logout", command=self.logout)
        menu.add_cascade(label="User", menu=user_menu)



    def create_login_screen(self):
        self.clear_screen()
        self.create_menu()

        # Background image
        self.background_image = PhotoImage(file="img_6.png")
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for login elements
        login_frame = tk.Frame(self.master, bg="white", width=300, height=200)
        login_frame.place(relx=0.2, rely=0.2)

        self.username_label = tk.Label(login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_btn = tk.Button(login_frame, text="Login", command=self.login)
        self.login_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.register_btn = tk.Button(login_frame, text="Register", command=self.create_register_screen)
        self.register_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def create_register_screen(self):
        self.clear_screen()
        self.create_menu()

        # Background image
        self.background_image = PhotoImage(file="img_6.png")
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for register elements
        register_frame = tk.Frame(self.master, bg="white", width=300, height=200)
        register_frame.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

        self.username_label = tk.Label(register_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(register_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(register_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(register_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.balance_label = tk.Label(register_frame, text="Initial Balance:")
        self.balance_label.grid(row=2, column=0, padx=10, pady=5)

        self.balance_entry = tk.Entry(register_frame)
        self.balance_entry.grid(row=2, column=1, padx=10, pady=5)

        self.register_btn = tk.Button(register_frame, text="Register", command=self.register)
        self.register_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.back_btn = tk.Button(register_frame, text="Back to Login", command=self.create_login_screen)
        self.back_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def create_main_menu(self):
        self.clear_screen()
        self.create_menu()

        # Change background image when user logs in
        self.background_image = PhotoImage(file="img_6.png")  # Change the filename as needed
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Buttons
        self.check_balance_btn = tk.Button(self.master, text="Check Balance", command=self.check_balance, bg="blue",
                                           fg="white")
        self.check_balance_btn.grid(row=0, column=0, padx=10, pady=10)

        self.transfer_btn = tk.Button(self.master, text="Transfer Funds", command=self.transfer_funds, bg="blue",
                                      fg="white")
        self.transfer_btn.grid(row=0, column=1, padx=10, pady=10)

        self.logout_btn = tk.Button(self.master, text="Logout", command=self.logout, bg="blue", fg="white")
        self.logout_btn.grid(row=0, column=2, padx=10, pady=10)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def login(self):

        # Change background image when user logs in
        self.background_image = PhotoImage(file="img_6.png")  # Change the filename as needed
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username]["password"] == password:
            self.logged_in_user = username
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        # Change background image when user logs in
        self.background_image = PhotoImage(file="img_6.png")  # Change the filename as needed
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        username = self.username_entry.get()
        password = self.password_entry.get()
        balance_str = self.balance_entry.get()

        try:
            balance = float(balance_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid balance amount")
            return

        if username not in self.users:
            self.users[username] = {"password": password, "balance": balance}
            messagebox.showinfo("Success", "Account registered successfully")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Username already exists")

    def check_balance(self):
        balance = self.users[self.logged_in_user]["balance"]
        messagebox.showinfo("Balance", f"Your balance is: ${balance}")

    def transfer_funds(self):
        self.clear_screen()
        self.create_menu()

        # Background image
        self.background_image = PhotoImage(file="img_6.png")
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for transfer elements
        transfer_frame = tk.Frame(self.master, bg="white", width=300, height=200)
        transfer_frame.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

        self.recipient_label = tk.Label(transfer_frame, text="Recipient:")
        self.recipient_label.grid(row=0, column=0, padx=10, pady=5)

        self.recipient_entry = tk.Entry(transfer_frame)
        self.recipient_entry.grid(row=0, column=1, padx=10, pady=5)

        self.amount_label = tk.Label(transfer_frame, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=5)

        self.amount_entry = tk.Entry(transfer_frame)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        self.transfer_btn = tk.Button(transfer_frame, text="Transfer", command=self.process_transfer)
        self.transfer_btn.grid(row=2, column=0, columnspan=2, padx=(10, 5), pady=10)  # Adjusted padx

        self.cancel_btn = tk.Button(transfer_frame, text="Cancel", command=self.create_main_menu)
        self.cancel_btn.grid(row=2, column=1, columnspan=2, padx=(5, 10), pady=10)  # Adjusted padx

    def process_transfer(self):
        recipient = self.recipient_entry.get()
        amount = float(self.amount_entry.get())

        if recipient in self.users and amount > 0:
            if self.logged_in_user != recipient:
                if self.users[self.logged_in_user]["balance"] >= amount:
                    self.users[self.logged_in_user]["balance"] -= amount
                    self.users[recipient]["balance"] += amount
                    messagebox.showinfo("Success", "Funds transferred successfully")
                else:
                    messagebox.showerror("Error", "Insufficient funds")
            else:
                messagebox.showerror("Error", "Cannot transfer funds to yourself")
        else:
            messagebox.showerror("Error", "Invalid recipient or amount")

    def logout(self):
        self.logged_in_user = None
        self.create_login_screen()


def main():
    root = tk.Tk()
    app = BankApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
