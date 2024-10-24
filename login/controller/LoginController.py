# controller.py
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from GestionePersonale.model.gestore import Gestore
from GestionePersonale.model.pt import PT

class LoginController:
    def __init__(self, view):
        self.view = view

    def handle_login(self, username, password):
        if Gestore.check_credentials_gestore(username, password):
            self.view.master.destroy()
            from login.view.gestore_view import MainView
            main_window = ctk.CTk() 
          # Imposta la finestra in modalità schermo intero
            main_window.title("Dashboard Gestore")
            MainView(main_window)   
            main_window.mainloop()
        else:
            if PT.check_credentials_gestore(username, password):
                self.view.master.destroy()
                from GestionePersonale.view.pt_view import PTView
                main_window = ctk.CTk() 
                  # Imposta la finestra in modalità schermo intero
                main_window.title("Dashboard PT")
                PTView(main_window)   
                main_window.mainloop()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

    