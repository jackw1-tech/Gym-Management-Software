import customtkinter as ctk
from GestionePalestra.view.aggiungi_corsi_view import AggiungiCorsiView
from GestionePalestra.model.corso import corso
from GestionePersonale.model.gestore import Gestore
from GestionePalestra.model.pacchetto import pacchetto

class pacchetto_controller:
    def __init__(self, master):
        self.master = master

    def open_course_package_search(self):
        from GestionePalestra.view.pacchetti_view import CoursePackageSearchView
        # Recupera i pacchetti di corsi, in un’applicazione reale, questi dati verrebbero recuperati dal database
        packages = self.get_course_packages()

        # Crea una nuova finestra per la ricerca dei pacchetti di corsi
        search_window = ctk.CTkToplevel(self.master)
        CoursePackageSearchView(search_window, packages)

    def get_course_packages(self):
        ids = Gestore.recupera_pacchetti_dal_documento_gestore()
        return pacchetto.recupera_pacchetti_da_ids(ids)
       
    
  
    
    def ciao(self,corsi_selezionati):
        from GestionePalestra.view.aggiungi_pacchetti_view import AggiungiPacchettoView
        print(corsi_selezionati)
        root = ctk.CTkToplevel()
        AggiungiPacchettoView(root, print("ciao"),corsi_selezionati)
        root.mainloop()
        
    def aggiungi_corso_view(self):
        corsi = Gestore.recupera_corsi_dal_documento_gestore()
        print(corsi)
        corsi_disponibili = corso.recupera_corsi_da_firebase(corsi)
        root = ctk.CTkToplevel()
        AggiungiCorsiView(root, corsi_disponibili, self.ciao)
        root.mainloop()

    def crea_pacchetto(self,nome,prezzo,corsi_selezionati):
        lista_doc_id_corsi = []
        for corso_str in corsi_selezionati:
            lista_doc_id_corsi.append(corso.get_document_id(corso_str))
        Pacchetto_nuovo = pacchetto(prezzo,nome,lista_doc_id_corsi)
        Pacchetto_nuovo.aggiungi_pacchetto_a_firebase()
   

    