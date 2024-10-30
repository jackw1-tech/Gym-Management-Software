import customtkinter as ctk
from GestionePalestra.view.aggiungi_corsi_view import AggiungiCorsiView
from GestionePalestra.model.corso import corso
from GestionePersonale.model.gestore import Gestore
from GestionePalestra.model.pacchetto import pacchetto


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
        print(corsi_selezionati)
        root = ctk.CTk()
        AggiungiPacchettoView(root,pacchetto_controller.open_course_package_search ,corsi_selezionati, pacchetto_controller.torna_indietro)
        root.mainloop()
        
    def aggiungi_corso_view(self):
        corsi = Gestore.recupera_corsi_dal_documento_gestore()
        print(corsi)
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
   

    