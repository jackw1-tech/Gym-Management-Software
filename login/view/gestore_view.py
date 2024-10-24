import customtkinter as ctk
from GestionePersonale.view.personale_view import PersonaleView

class MainView:
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

        self.button_personale = ctk.CTkButton(master, text="Personale", command=self.open_personale)
        self.button_personale.pack(pady=10)

        self.button_palestra = ctk.CTkButton(master, text="Palestra", command=self.open_palestra)
        self.button_palestra.pack(pady=10)

        self.button_contabilita = ctk.CTkButton(master, text="Contabilità", command=self.open_contabilita)
        self.button_contabilita.pack(pady=10)

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

    def open_contabilita(self):
        print("Apertura schermata Contabilità")

    def go_back_home(self):
        # Riporta l'utente alla schermata principale (home)
        home_window = ctk.CTk()
        MainView(home_window)  # Riapre la schermata della dashboard
        home_window.mainloop()