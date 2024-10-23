# view.py
import tkinter as tk
from login.controller.LoginController import LoginController


class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Management Software - Login")
        self.master.geometry("300x150")

       
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

    
        self.controller = LoginController(self)

    
        self.login_button = tk.Button(master, text="Login", command=self.on_login_button_click)
        self.login_button.pack(pady=10)

    def on_login_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.handle_login(username, password)


