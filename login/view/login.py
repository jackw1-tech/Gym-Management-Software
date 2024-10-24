import customtkinter as ctk
from tkinter import messagebox
from login.controller.LoginController import LoginController

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Management Software - Login")
        self.master.geometry("400x300")

        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Label del titolo
        self.label_title = ctk.CTkLabel(master, text="Login", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Campo Username
        self.label_username = ctk.CTkLabel(master, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(master, width=200)
        self.entry_username.pack(pady=5)

        # Campo Password
        self.label_password = ctk.CTkLabel(master, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(master, width=200, show="*")  # show="*" nasconde la password
        self.entry_password.pack(pady=5)

        self.controller = LoginController(self)

        # Pulsante di login
        self.login_button = ctk.CTkButton(master, text="Login", command=self.on_login_button_click)
        self.login_button.pack(pady=20)

    def on_login_button_click(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.handle_login(username, password)