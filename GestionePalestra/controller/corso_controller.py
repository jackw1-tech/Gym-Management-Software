import customtkinter as ctk

from GestionePalestra.model.corso import corso



class corso_controller:
    def __init__(self, master):
        self.master = master

    def crea_corso(self, nome,descrizione):
        nuovo_corso = corso(nome,descrizione)
        nuovo_corso.carica_corso_su_firebase()
        
        
        
        
        
        
   

    