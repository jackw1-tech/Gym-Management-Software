# controller.py
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from GestionePersonale.model.gestore import Gestore
from GestionePersonale.model.pt import PT


class PTController:
    def __init__(self, view):
        self.view = view
    
    def crea_pt(self, nome, cognome, stipendio,username,password):
        pt = PT(nome,cognome,stipendio,username,password)
        pt.salva_su_firebase()
        print(pt)

    def get_view_trova_pt(self):
        from GestionePalestra.view.trova_pt_view import PersonalTrainerSearchView
        personal_trainers = Gestore.get_lista_pt(self)
        root = ctk.CTk()
        PersonalTrainerSearchView(root, personal_trainers)
        root.mainloop()