from tkinter import messagebox
import customtkinter as ctk
from GestionePalestra.controller.corso_controller import corso_controller

class CreaCorsoView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Aggiungi Nuovo Corso")
        self.master.geometry("700x600")
        self.corso_controller = corso_controller(self)
        

        # Impostazione del tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Creazione del frame scorrevole
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=360)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Titolo della schermata
        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Aggiungi Nuovo Corso", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Campi di inserimento
        self.label_nome = ctk.CTkLabel(self.scrollable_frame, text="Nome del Corso:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il nome del corso")
        self.entry_nome.pack(pady=5)

        self.label_descrizione = ctk.CTkLabel(self.scrollable_frame, text="Descrizione del Corso:")
        self.label_descrizione.pack(pady=5)
        self.entry_descrizione = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la descrizione del corso")
        self.entry_descrizione.pack(pady=5)


        # Pulsante per registrare il corso
        self.button_registra = ctk.CTkButton(self.scrollable_frame, text="Registra Corso", command=lambda:self.registra_corso(home_callback))
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
        self.master.destroy()
        funzione(self)

    def registra_corso(self, funzione):
        nome = self.entry_nome.get()
        descrizione = self.entry_descrizione.get()
        self.corso_controller.crea_corso(nome,descrizione)
        messagebox.showinfo("Successo", "Corso creato con successo")
        
        self.master.destroy()
        funzione(self)
        
        
       
        
        

