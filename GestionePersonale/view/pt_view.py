import customtkinter as ctk

class PTView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Palestra - Dashboard")
        self.master.geometry("600x400")

        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Label del titolo
        self.label_title = ctk.CTkLabel(master, text="Dashboard", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Creazione dei pulsanti
        self.button_clienti = ctk.CTkButton(master, text="Clienti", command=self.open_clienti)
        self.button_clienti.pack(pady=10)

        self.button_corsi = ctk.CTkButton(master, text="Corsi", command=self.open_corsi)
        self.button_corsi.pack(pady=10)

        self.button_palestra = ctk.CTkButton(master, text="Palestra", command=self.open_palestra)
        self.button_palestra.pack(pady=10)

    # Funzioni placeholder per i pulsanti
    def open_clienti(self):
        print("Apertura schermata Clienti")

    def open_corsi(self):
        print("Apertura schermata Corsi")

    def open_palestra(self):
        print("Apertura schermata Palestra")