import customtkinter as ctk
from GestionePalestra.view.aggiungi_corsi_view import AggiungiCorsiView
from GestionePalestra.model.corso import corso
from GestionePersonale.model.gestore import Gestore
from GestionePalestra.model.pacchetto import pacchetto
from GestionePalestra.view.dettagli_pacchetto_view import PacchettoDetailsView
from GestionePalestra.view.modifica_pacchetto_view import ModificaPacchettoView

class pacchetto_controller:
    def __init__(self, master):
        self.master = master

    def torna_indietro():
        from login.view.gestore_view import MainView
        home_window = ctk.CTk()
        MainView(home_window)  
        home_window.mainloop()
        
    def open_course_package_search(self):
        from GestionePalestra.view.pacchetti_view import CoursePackageSearchView
        packages = self.get_course_packages()
        CoursePackageSearchView(self.master, packages, pacchetto_controller.torna_indietro)

    def get_course_packages(self):
        ids = Gestore.recupera_pacchetti_dal_documento_gestore()
        return pacchetto.recupera_pacchetti_da_ids(ids)
       
    
    
    
    def ciao(self,corsi_selezionati):
        from GestionePalestra.view.aggiungi_pacchetti_view import AggiungiPacchettoView
        root = ctk.CTk()
        AggiungiPacchettoView(root,pacchetto_controller.open_course_package_search ,corsi_selezionati, pacchetto_controller.torna_indietro)
        root.mainloop()
        
    def aggiungi_corso_view(self):
        corsi = Gestore.recupera_corsi_dal_documento_gestore()
        corsi_disponibili = corso.recupera_corsi_da_firebase(corsi)
        root = ctk.CTk()
        AggiungiCorsiView(root, corsi_disponibili, self.ciao)
        root.mainloop()

    def crea_pacchetto(self,nome,prezzo,corsi_selezionati):
        lista_doc_id_corsi = []
        for corso_str in corsi_selezionati:
            lista_doc_id_corsi.append(corso.get_document_id(corso_str))
        Pacchetto_nuovo = pacchetto(prezzo,nome,lista_doc_id_corsi)
        Pacchetto_nuovo.aggiungi_pacchetto_a_firebase()
   

    def elimina_pacchetto_view(self,id, funzione):
        pacchetto.rimuovi_pacchetto_da_firebase(id)
        Gestore.elimina_pacchetto_da_lista_gestore(id)
        funzione()
        
    def dettagli_pacchetto_view(self, id_pacchetto):
        dettagli_pacchetto = pacchetto.recupera_dettagli_pacchetto(id_pacchetto)
        if dettagli_pacchetto:
            nome = dettagli_pacchetto["nome"]
            prezzo = dettagli_pacchetto["prezzo"]
            corsi = dettagli_pacchetto["lista_corsi"]
            lista_corsi = corso.recupera_corsi_da_firebase(corsi)
            root = ctk.CTk()
            app = PacchettoDetailsView(root, lista_corsi,nome,prezzo)
            app.center_window()
            root.mainloop()
    
    def corsi_selezionati_callback(id_pacchetto, corsi_selezionati, nome_nuovo, prezzo_nuovo_float):
        from login.view.gestore_view import MainView
        pacchetto.modifica_pacchetto(id_pacchetto,corsi_selezionati,nome_nuovo,prezzo_nuovo_float)
        home_window = ctk.CTk()
        MainView(home_window)  
        home_window.mainloop()
        

     
   
    def modifica_pacchetto_view(self, id_pacchetto):
        dettagli_pacchetto = pacchetto.recupera_dettagli_pacchetto(id_pacchetto)
        if dettagli_pacchetto:
            nome = dettagli_pacchetto["nome"]
            prezzo = dettagli_pacchetto["prezzo"]
            corsi = dettagli_pacchetto["lista_corsi"]
            lista_corsi_pacchetto = corso.recupera_corsi_da_firebase(corsi)
            lista_corsi_disponibili = corso.recupera_corsi_da_firebase_escludendo_ids(corsi)
            root = ctk.CTk()
            app = ModificaPacchettoView(root, lista_corsi_disponibili, lista_corsi_pacchetto, pacchetto_controller.corsi_selezionati_callback, nome, prezzo, id_pacchetto, pacchetto_controller.torna_indietro)

            root.mainloop() 

        