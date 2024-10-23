# controller.py
import tkinter as tk
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
            main_window = tk.Tk()  
            MainView(main_window)   
            main_window.mainloop()
        else:
            if PT.check_credentials_gestore(username, password):
                self.view.master.destroy()
                from GestionePersonale.view.pt_view import PTView
                main_window = tk.Tk()  
                PTView(main_window)   
                main_window.mainloop()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")