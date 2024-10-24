import customtkinter as ctk

class AggiungiPTView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Aggiungi Personal Trainer")
        self.master.geometry("600x400")

        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Label del titolo
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Creazione dei campi per l'inserimento dei dati
        self.label_nome = ctk.CTkLabel(master, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(master, placeholder_text="Inserisci il nome")
        self.entry_nome.pack(pady=5)

        self.label_cognome = ctk.CTkLabel(master, text="Cognome:")
        self.label_cognome.pack(pady=5)
        self.entry_cognome = ctk.CTkEntry(master, placeholder_text="Inserisci il cognome")
        self.entry_cognome.pack(pady=5)

        self.label_stipendio = ctk.CTkLabel(master, text="Stipendio:")
        self.label_stipendio.pack(pady=5)
        self.entry_stipendio = ctk.CTkEntry(master, placeholder_text="Inserisci lo stipendio")
        self.entry_stipendio.pack(pady=5)

        self.label_username = ctk.CTkLabel(master, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(master, placeholder_text="Inserisci lo username")
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(master, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(master, placeholder_text="Inserisci la password", show="*")
        self.entry_password.pack(pady=5)

        # Pulsante Registra
        self.button_registra = ctk.CTkButton(master, text="Registra", command=self.registra_pt)
        self.button_registra.pack(pady=10)

        # Pulsante per tornare alla Home
        self.button_back_home = ctk.CTkButton(master, text="Torna alla Home", command=lambda: self.torno_alla_home(home_callback))
        self.button_back_home.pack(pady=10)

    def torno_alla_home(self, funzione):
        self.master.destroy()  # Chiude la finestra corrente
        funzione()  # Richiama il callback passato (torna alla home)

    def registra_pt(self):
        # Qui si gestisce la logica per registrare un nuovo personal trainer
        nome = self.entry_nome.get()
        cognome = self.entry_cognome.get()
        stipendio = self.entry_stipendio.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        print(f"Registrazione PT: Nome={nome}, Cognome={cognome}, Stipendio={stipendio}, Username={username}")
