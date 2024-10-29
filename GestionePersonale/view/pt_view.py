import customtkinter as ctk

class PTView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Palestra - Dashboard")
        self.master.geometry("600x500")
       

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
        
        self.center_window()

    def center_window(self):
        # Calcolare la larghezza e l'altezza dello schermo
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calcolare le dimensioni della finestra
        window_width = 600
        window_height = 500

        # Calcolare la posizione x e y per centrare la finestra
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Impostare la geometria della finestra
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")


    # Funzioni placeholder per i pulsanti
    def open_clienti(self):
        print("Apertura schermata Clienti")

    def open_corsi(self):
        print("Apertura schermata Corsi")

    def open_palestra(self):
        print("Apertura schermata Palestra")