
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from GestionePersonale.model.gestore import Gestore
from GestionePersonale.model.pt import PT
import customtkinter as ctk


class LoginController:
    def __init__(self, view):
        self.view = view

    def handle_registration():
        from login.view.registrazione_gestore import registra_gestore_view
        from login.view.login import LoginScreen  
        if Gestore.verifica_esistenza_gestore():
            root = ctk.CTk() 
            LoginScreen(root)
            root.mainloop()
        else:
            root = ctk.CTk() 
            registra_gestore_view(root, LoginController.handle_registration)
            root.mainloop()
        
    def handle_login(self, username, password):
        if Gestore.check_credentials_gestore(self, username, password):
            self.view.master.destroy()
            from login.view.gestore_view import MainView
            main_window = ctk.CTk() 
            main_window.title("Dashboard Gestore")
            MainView(main_window)   
            
           
        else:
            success, pt_instance = PT.check_credentials_gestore(username, password)
            if success:
                self.view.master.destroy()
                from GestionePersonale.view.pt_view import PTView
                main_window = ctk.CTk() 
                PTView(main_window, pt_instance)  
            
            else:
                messagebox.showerror("Autenticazione fallita", "Username o password errati")
             
               
            
    