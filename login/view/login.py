import customtkinter as ctk
from tkinter import messagebox
from login.controller.LoginController import LoginController

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Management Software - Login")
       
        
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue")  

       
        self.label_title = ctk.CTkLabel(master, text="Login", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        
        self.label_username = ctk.CTkLabel(master, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(master, width=200)
        self.entry_username.pack(pady=5)

        
        self.label_password = ctk.CTkLabel(master, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(master, width=200, show="*")
        self.entry_password.pack(pady=5)

        self.controller = LoginController(self)

       
        self.login_button = ctk.CTkButton(master, text="Login", command=self.on_login_button_click)
        self.login_button.pack(pady=20)

        self.center_window()

    def center_window(self):
  
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        
        window_width = 700
        window_height = 600

     
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

       
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_login_button_click(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.handle_login(username, password)
