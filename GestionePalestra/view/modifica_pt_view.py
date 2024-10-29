import customtkinter as ctk
from GestionePersonale.controller.pt_controller import PTController
from GestionePersonale.model.pt import PT

class ModificaPTView:
    def __init__(self, master, home_callback, trainer_data):
        self.master = master
        self.master.title("Modifica Personal Trainer")
        self.master.geometry("700x600")
        self.controller = PTController(self)
        self.trainer_data = trainer_data  # Dati esistenti del PT

        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Creazione di un frame scorrevole
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=550)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Label del titolo
        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Modifica Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Creazione dei campi per la modifica dei dati
        self.label_nome = ctk.CTkLabel(self.scrollable_frame, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il nome")
        self.entry_nome.insert(0, trainer_data['nome'])  # Pre-riempi con il nome esistente
        self.entry_nome.pack(pady=5)

        self.label_cognome = ctk.CTkLabel(self.scrollable_frame, text="Cognome:")
        self.label_cognome.pack(pady=5)
        self.entry_cognome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il cognome")
        self.entry_cognome.insert(0, trainer_data['cognome'])  # Pre-riempi con il cognome esistente
        self.entry_cognome.pack(pady=5)

        self.label_stipendio = ctk.CTkLabel(self.scrollable_frame, text="Stipendio:")
        self.label_stipendio.pack(pady=5)
        self.entry_stipendio = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci lo stipendio")
        self.entry_stipendio.insert(0, trainer_data['stipendio'])  # Pre-riempi con lo stipendio esistente
        self.entry_stipendio.pack(pady=5)

        self.label_username = ctk.CTkLabel(self.scrollable_frame, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci lo username")
        self.entry_username.insert(0, trainer_data['username'])  # Pre-riempi con lo username esistente
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.scrollable_frame, text="Password (obbligatoria):")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la password", show="*")
        
        self.entry_password.pack(pady=5)

        # Menu a discesa per selezionare lo stato
        self.label_stato = ctk.CTkLabel(self.scrollable_frame, text="Stato:")
        self.label_stato.pack(pady=5)

        # Opzioni per lo stato
        stati = ["Inattivo", "In ferie", "Disponibile"]
        self.optionmenu_stato = ctk.CTkOptionMenu(self.scrollable_frame, values=stati, command=self.on_stato_change)
        self.optionmenu_stato.set(trainer_data['stato'])  # Imposta il valore di default in base allo stato del PT
        self.optionmenu_stato.pack(pady=5)

        # Campi per le date di inizio e fine ferie (inizialmente nascosti)
        self.label_data_inizio = ctk.CTkLabel(self.scrollable_frame, text="Data inizio ferie:")
        self.entry_data_inizio = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la data di inizio")
        
        self.label_data_fine = ctk.CTkLabel(self.scrollable_frame, text="Data fine ferie:")
        self.entry_data_fine = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la data di fine")

        # Mostra i campi delle date se lo stato è già "In ferie"
        if trainer_data['stato'] == "In ferie":
            self.mostra_campi_ferie()

        # Pulsante per salvare le modifiche
        self.button_salva = ctk.CTkButton(self.scrollable_frame, text="Salva Modifiche", command=lambda: self.salva_modifiche_pt(home_callback))
        self.button_salva.pack(pady=10)

        # Pulsante per tornare alla Home
        self.button_back_home = ctk.CTkButton(self.scrollable_frame, text="Torna alla Home", command=lambda: self.torna_alla_home(home_callback))
        self.button_back_home.pack(pady=10)
        
    def center_window(self):
       # Calcolare la larghezza e l'altezza dello schermo
       screen_width = self.master.winfo_screenwidth()
       screen_height = self.master.winfo_screenheight()

       # Calcolare le dimensioni della finestra
       window_width = 700
       window_height = 600

       # Calcolare la posizione x e y per centrare la finestra
       x = (screen_width // 2) - (window_width // 2)
       y = (screen_height // 2) - (window_height // 2)

       # Impostare la geometria della finestra
       self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_stato_change(self, stato_selezionato):
       # Mostra o nasconde i campi delle date di ferie in base allo stato selezionato
       if stato_selezionato == "In ferie":
           self.mostra_campi_ferie()
       else:
           self.nascondi_campi_ferie()

    def mostra_campi_ferie(self):
       self.label_data_inizio.pack(pady=5)
       self.entry_data_inizio.pack(pady=5)
       self.label_data_fine.pack(pady=5)
       self.entry_data_fine.pack(pady=5)

    def nascondi_campi_ferie(self):
       self.label_data_inizio.pack_forget()
       self.entry_data_inizio.pack_forget()
       self.label_data_fine.pack_forget()
       self.entry_data_fine.pack_forget()

    def torna_alla_home(self, funzione):
       funzione()  # Richiama il callback passato (torna alla home)

    def salva_modifiche_pt(self, funzione):
       nome = self.entry_nome.get()
       cognome = self.entry_cognome.get()
       stipendio = self.entry_stipendio.get()
       username = self.entry_username.get()
       password = self.entry_password.get()
       
       if not password:  # Controllo se la password è vuota
           ctk.CTkMessageBox.show_error("Errore", "La password è obbligatoria!")
           return

       stato = self.optionmenu_stato.get()

       
       if stato == "In ferie":
           data_inizio = self.entry_data_inizio.get()
           data_fine = self.entry_data_fine.get()
           print(f"In ferie dal {data_inizio} al {data_fine}")
       else:
           data_inizio = None
           data_fine = None

       
       PT.aggiorna_dati(self.controller, 
                        id=self.trainer_data['id'], 
                        nome=nome,
                        cognome=cognome,
                        stipendio=stipendio,
                        username=username,
                        password=password,
                        stato=stato,
                        data_inizio=data_inizio,
                        data_fine=data_fine)
       
       print(f"Modifiche salvate per {nome} {cognome}")
       self.master.destroy() 
       funzione()  # Richiama il callback passato (torna alla home)
