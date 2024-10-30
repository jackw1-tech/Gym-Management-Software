from tkinter import messagebox
import customtkinter as ctk
from GestionePersonale.controller.pt_controller import PTController

class AggiungiPTView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Aggiungi Personal Trainer")
        self.master.geometry("700x600")
        self.controller = PTController(self)

        # Impostare la modalità del tema e i colori
        ctk.set_appearance_mode("dark")  # Imposta il tema scuro
        ctk.set_default_color_theme("blue")  # Imposta il tema del colore

        # Creazione di un frame scorrevole
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=360)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Label del titolo
        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Aggiungi Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Creazione dei campi per l'inserimento dei dati
        self.label_nome = ctk.CTkLabel(self.scrollable_frame, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il nome")
        self.entry_nome.pack(pady=5)

        self.label_cognome = ctk.CTkLabel(self.scrollable_frame, text="Cognome:")
        self.label_cognome.pack(pady=5)
        self.entry_cognome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il cognome")
        self.entry_cognome.pack(pady=5)

        self.label_stipendio = ctk.CTkLabel(self.scrollable_frame, text="Stipendio:")
        self.label_stipendio.pack(pady=5)
        self.entry_stipendio = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci lo stipendio")
        self.entry_stipendio.pack(pady=5)

        self.label_username = ctk.CTkLabel(self.scrollable_frame, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci lo username")
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.scrollable_frame, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la password", show="*")
        self.entry_password.pack(pady=5)

        # Pulsante Registra
        self.button_registra = ctk.CTkButton(self.scrollable_frame, text="Registra", command=lambda: self.registra_pt(home_callback))
        self.button_registra.pack(pady=10)

        # Pulsante per tornare alla Home
        self.button_back_home = ctk.CTkButton(self.scrollable_frame, text="Torna alla Home", command=lambda: self.torno_alla_home(home_callback))
        self.button_back_home.pack(pady=10)
        self.center_window()

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


    def torno_alla_home(self, funzione):
        self.master.destroy()  # Chiude la finestra corrente
        funzione()  # Richiama il callback passato (torna alla home)

    def registra_pt(self,funzione):
        nome = self.entry_nome.get()
        cognome = self.entry_cognome.get()
        stipendio = self.entry_stipendio.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        # Chiamata al controller per creare il Personal Trainer
        self.controller.crea_pt(nome,cognome,stipendio,username,password)
        messagebox.showinfo("Successo", "Pt registrato con successo")
        funzione()