import customtkinter as ctk
from GestionePersonale.view.aggiungi_pt_view import AggiungiPTView
from GestionePersonale.controller.pt_controller import PTController
class PersonaleView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Gestione Personal Trainer")
        self.master.geometry("600x400")
        self.controller = PTController(self)

        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Label del titolo
        self.label_title = ctk.CTkLabel(master, text="Gestione Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Creazione dei pulsanti
        self.button_add_pt = ctk.CTkButton(master, text="Aggiungi PT", command=lambda: self.add_pt(home_callback))
        self.button_add_pt.pack(pady=10)

        self.button_find_pt = ctk.CTkButton(master, text="Trova PT", command= self.find_pt)
        self.button_find_pt.pack(pady=10)

        # Pulsante per tornare alla Home
        self.button_back_home = ctk.CTkButton(master, text="Torna alla Home", command=lambda: self.torno_alla_home(home_callback))
        self.button_back_home.pack(pady=10)

    def torno_alla_home(self, funzione):
        self.master.destroy()  # Chiude la finestra corrente
        funzione()  # Richiama il callback passato (torna alla home)

    # Funzioni placeholder per i pulsanti
    def add_pt(self,funzione):
        print("Apertura schermata per aggiungere PT")
        self.master.destroy()  # Chiude la finestra della dashboard
        main_window = ctk.CTk()  # Crea una nuova finestra
        AggiungiPTView(main_window, home_callback= funzione)  # Apre la schermata del personale con il pulsante Torna alla Home
        main_window.mainloop()

    def find_pt(self):
        self.controller.get_view_trova_pt()
        print("Apertura schermata per trovare PT")
        

        