import customtkinter as ctk
from GestionePersonale.view.aggiungi_pt_view import AggiungiPTView
from GestionePersonale.controller.pt_controller import PTController
class PersonaleView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Gestione Personal Trainer")
        self.master.geometry("600x500")
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
        self.master.destroy()
        self.controller.get_view_trova_pt()
        
        

        