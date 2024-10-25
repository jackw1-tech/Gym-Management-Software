import customtkinter as ctk
from GestionePalestra.controller.pacchetto_controller import pacchetto_controller

class PalestraView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Gestione Palestra")
        self.master.geometry("600x400")
        self.controller = pacchetto_controller(self)


        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Label del titolo
        self.label_title = ctk.CTkLabel(master, text="Gestione Palestra", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Creazione dei pulsanti
        self.button_orari = ctk.CTkButton(master, text="Orari", command=self.visualizza_orari)
        self.button_orari.pack(pady=10)

        self.button_pacchetti = ctk.CTkButton(master, text="Pacchetti", command=self.visualizza_pacchetti)
        self.button_pacchetti.pack(pady=10)

        self.button_corsi = ctk.CTkButton(master, text="Corsi", command=self.visualizza_corsi)
        self.button_corsi.pack(pady=10)

        # Pulsante per tornare alla Home
        self.button_back_home = ctk.CTkButton(master, text="Torna alla Home", command=lambda: self.torno_alla_home(home_callback))
        self.button_back_home.pack(pady=10)

    def torno_alla_home(self, funzione):
        self.master.destroy()  # Chiude la finestra corrente
        funzione()  # Richiama il callback passato (torna alla home)

    # Funzioni placeholder per i pulsanti
    def visualizza_orari(self):
        print("Visualizzazione degli orari della palestra")

    def visualizza_pacchetti(self):
        print("Visualizzazione dei pacchetti disponibili")
        # Usa direttamente la finestra esistente, senza creare un'altra finestra principale
        controller = pacchetto_controller(self.master)  # Passa la finestra principale esistente
        controller.open_course_package_search()
    
    def visualizza_corsi(self):
        print("Visualizzazione dei corsi disponibili")
