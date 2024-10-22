import tkinter as tk
from tkinter import messagebox

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Management Software - Login")
        self.master.geometry("300x150")

        # Username
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        # Password
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")  # The show="*" makes the password hidden
        self.password_entry.pack()

        # Login button
     
        self.login_button = tk.Button(master, text="Login", command=self.login)  # Qui creiamo il pulsante
        self.login_button.pack(pady=10)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Here you would typically check the username and password against your database
        # For this example, we'll use a simple check
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome to the Gym Management System!")
            self.master.destroy()  # Close the login window
            # Here you would typically open your main application window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    login_screen = LoginScreen(root)
    root.mainloop()
