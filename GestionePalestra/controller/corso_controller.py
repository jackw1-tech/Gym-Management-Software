import customtkinter as ctk

from GestionePalestra.model.corso import corso
from firebase_admin import credentials, firestore
from GestionePersonale.model.gestore import Gestore


db = firestore.client()
class corso_controller:
    def __init__(self, master):
        self.master = master

    def crea_corso(self, nome,descrizione):
        nuovo_corso = corso(nome,descrizione)
        nuovo_corso.carica_corso_su_firebase()
        
    def sezione_corsi_view(self):
        from GestionePalestra.view.corso_view import CourseSearchView
        corsi_ids = Gestore.recupera_corsi_dal_documento_gestore()
        corsi = corso.recupera_corsi_da_firebase(corsi_ids)
        home_window = ctk.CTk()
        CourseSearchView(home_window, corsi, corso_controller.home_callback)  
        home_window.mainloop()

    def home_callback(self):
        from login.view.gestore_view import MainView
        home_window = ctk.CTk()
        MainView(home_window)  
        home_window.mainloop()
    
    def crea_corso_view(self):
        from GestionePalestra.view.crea_corso_view import CreaCorsoView
        home_window = ctk.CTk()
        CreaCorsoView(home_window, corso_controller.home_callback)
        home_window.mainloop()
    
    def elimina_corso_view(self,id, funzione):
        from GestionePalestra.model.pacchetto import pacchetto
        from GestionePersonale.model.pt import PT
        corso.rimuovi_corso_da_firebase(id)
        Gestore.elimina_corso_da_lista_gestore(id)
        pacchetto.rimuovi_corso_da_pacchetti(id)
        PT.rimuovi_corso_da_pt(id)
        funzione(self)
        
    def dettagli_corso_view(self, id_corso):
        from GestionePersonale.model.pt import PT
        from GestionePalestra.view.dettagli_corso_view import CorsoDetailsView
        
        dettagli_corso = corso.recupera_dettagli_corso(id_corso)
        if dettagli_corso:
            nome = dettagli_corso["nome"]
            descrizione = dettagli_corso["descrizione"]
            pt = dettagli_corso["pt_assegnato"]
            lista_pt = PT.ottieni_dati_pt(pt)
            root = ctk.CTk()
            app = CorsoDetailsView(root, lista_pt,nome,descrizione)
            app.center_window()
            root.mainloop()
            
    def pt_selezionati_callback(id_corso, pt_selezionati, nome_nuovo, nuova_descrizione):
        from GestionePersonale.model.pt import PT
        from login.view.gestore_view import MainView
        corso.modifica_corso(id_corso,pt_selezionati,nome_nuovo,nuova_descrizione)
        PT.rimuovi_corso_da_pt(id_corso)
        for pt in pt_selezionati:
            PT.aggiorna_corsi_pt(str(pt['id']), id_corso, "+")
        home_window = ctk.CTk()
        MainView(home_window)  
        home_window.mainloop()
        
    def torna_indietro():
        from login.view.gestore_view import MainView
        home_window = ctk.CTk()
        MainView(home_window)  
        home_window.mainloop()
        
    def modifica_corso_view(self, id_corso):
        from GestionePersonale.model.pt import PT
        from GestionePalestra.view.modifica_corso_view import ModificaCorsoView
        dettagli_corso = corso.recupera_dettagli_corso(id_corso)
        if dettagli_corso:
            nome = dettagli_corso["nome"]
            descrizione = dettagli_corso["descrizione"]
            pt = dettagli_corso["pt_assegnato"]
            lista_pt = PT.ottieni_dati_pt(pt)
            root = ctk.CTk()
            app = ModificaCorsoView(root,nome,descrizione,lista_pt,corso_controller.pt_selezionati_callback,id_corso,corso_controller.torna_indietro)
            root.mainloop() 
        
        
        
    
        
        
        
        
   

    