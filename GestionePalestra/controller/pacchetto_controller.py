import customtkinter as ctk
from GestionePalestra.view.pacchetti_view import CoursePackageSearchView
from GestionePalestra.view.aggiungi_pacchetti_view import AggiungiCorsiView

class pacchetto_controller:
    def __init__(self, master):
        self.master = master

    def open_course_package_search(self):
        # Recupera i pacchetti di corsi, in un’applicazione reale, questi dati verrebbero recuperati dal database
        packages = self.get_course_packages()

        # Crea una nuova finestra per la ricerca dei pacchetti di corsi
        search_window = ctk.CTkToplevel(self.master)
        CoursePackageSearchView(search_window, packages)

    def get_course_packages(self):
        # Simulazione di dati dei pacchetti di corsi per il test
        return [
            {"nome": "Pacchetto Yoga", "id": "pkg1"},
            {"nome": "Pacchetto Crossfit", "id": "pkg2"},
            {"nome": "Pacchetto Pilates", "id": "pkg3"},
            {"nome": "Pacchetto Cardio", "id": "pkg4"},
            {"nome": "Pacchetto Strength", "id": "pkg5"},
            {"nome": "Pacchetto HIIT", "id": "pkg6"},
        ]
    
    def corsi_selezionati_callback(corsi):
    # Logica per gestire i corsi selezionati (es. salvarli nel pacchetto)
        for corso in corsi:
            print(f"Corso selezionato: {corso['nome']}")

    # Dati fittizi di corsi disponibili
    corsi_disponibili = [
        {"nome": "Yoga", "id": "corso1"},
        {"nome": "Crossfit", "id": "corso2"},
        {"nome": "Pilates", "id": "corso3"},
        {"nome": "Cardio", "id": "corso4"},
        {"nome": "Strength", "id": "corso5"},
    ]

    # In qualche parte del codice
    root = ctk.CTkToplevel()
    AggiungiCorsiView(root, corsi_disponibili, corsi_selezionati_callback)
    root.mainloop()