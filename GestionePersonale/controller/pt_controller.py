# controller.py
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from GestionePersonale.model.gestore import Gestore
from GestionePersonale.model.pt import PT
from GestionePalestra.model.corso import corso





class PTController:
    def __init__(self, view):
        self.view = view
    
    def crea_pt(self, nome, cognome, stipendio,username,password):
        pt = PT(nome,cognome,stipendio,username,password)
        pt.salva_su_firebase()
        
    def go_back_home():
        from login.view.gestore_view import MainView
        home_window = ctk.CTk()
        MainView(home_window)  # Riapre la schermata della dashboard
        home_window.mainloop()
        
    def torna_gestione_personal_trainer_by_gestore():
        from GestionePersonale.view.personale_view import PersonaleView
        main_window = ctk.CTk()  # Crea una nuova finestra
        PersonaleView(main_window, home_callback=PTController.go_back_home)  # Apre la schermata del personale con il pulsante Torna alla Home
        main_window.mainloop()
        
    def get_view_trova_pt(self):
        from GestionePalestra.view.trova_pt_view import PersonalTrainerSearchView
        personal_trainers = Gestore.get_lista_pt(self)
        root = ctk.CTk()
        PersonalTrainerSearchView(root, personal_trainers, PTController.torna_gestione_personal_trainer_by_gestore)
        root.mainloop()
        
    def assegna_corso_pt(self, pt_id, corso_id, tipo):
        PT.aggiorna_corsi_pt(str(pt_id), str(corso_id), str(tipo))
        corso.aggiorna_pt_al_corso(str(pt_id), str(corso_id), str(tipo))
        
    
    def assegna_corsi_view(self, id_pt):
        from GestionePalestra.view.assegna_corso_pt import AssegnaCorsiView
        root = ctk.CTk() 
        lista_corsi = PT.ottieni_corsi_attuali_pt(id_pt)
        lista_corsi_disponibili = PT.ottieni_corsi_non_attuali_pt(id_pt)
        AssegnaCorsiView(root, pt_id=id_pt, corsi_attuali=lista_corsi, corsi_disponibili=lista_corsi_disponibili, assegna_corso_callback=PTController.assegna_corso_pt, back_callback=PTController.get_view_trova_pt )
        root.mainloop()
            