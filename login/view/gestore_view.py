import customtkinter as ctk
from GestionePersonale.view.personale_view import PersonaleView
from GestionePalestra.view.palestra_view import PalestraView

class MainView:
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

        self.button_personale = ctk.CTkButton(master, text="Personale", command=self.open_personale)
        self.button_personale.pack(pady=10)

        self.button_palestra = ctk.CTkButton(master, text="Palestra", command=self.open_palestra)
        self.button_palestra.pack(pady=10)

        self.button_contabilita = ctk.CTkButton(master, text="Contabilità", command=self.open_contabilita)
        self.button_contabilita.pack(pady=10)

        # Centrare la finestra dopo che è stata creata
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

    def open_personale(self):
        self.master.destroy()  # Chiude la finestra della dashboard
        main_window = ctk.CTk()  # Crea una nuova finestra
        PersonaleView(main_window, home_callback=self.go_back_home)  # Apre la schermata del personale con il pulsante Torna alla Home
        main_window.mainloop()

    def open_palestra(self):
        print("Apertura schermata Palestra")
        self.master.destroy()  # Chiude la finestra della dashboard
        main_window = ctk.CTk()  # Crea una nuova finestra
        PalestraView(main_window, home_callback=self.go_back_home)  # Apre la schermata del personale con il pulsante Torna alla Home
        main_window.mainloop()

    def open_contabilita(self):
        print("Apertura schermata Contabilità")

    def go_back_home(self):
        # Riporta l'utente alla schermata principale (home)
        home_window = ctk.CTk()
        MainView(home_window)  # Riapre la schermata della dashboard
        home_window.mainloop()
