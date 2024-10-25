import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.controller.pacchetto_controller import pacchetto_controller

class AggiungiPacchettoView:
    def __init__(self, master, aggiungi_pacchetto_callback):
        self.master = master
        self.master.title("Aggiungi Pacchetto di Corsi")
        self.master.geometry("400x400")
        self.aggiungi_pacchetto_callback = aggiungi_pacchetto_callback
        self.pachetto_controller = 

        # Imposta il tema e i colori
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Titolo della schermata
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Pacchetto", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Campo Nome Pacchetto
        self.label_nome = ctk.CTkLabel(master, text="Nome Pacchetto:", font=ctk.CTkFont(size=14))
        self.label_nome.pack(pady=10)
        self.entry_nome = ctk.CTkEntry(master, placeholder_text="Inserisci nome pacchetto")
        self.entry_nome.pack(pady=10)

        # Campo Prezzo Pacchetto
        self.label_prezzo = ctk.CTkLabel(master, text="Prezzo Pacchetto (€):", font=ctk.CTkFont(size=14))
        self.label_prezzo.pack(pady=10)
        self.entry_prezzo = ctk.CTkEntry(master, placeholder_text="Inserisci prezzo pacchetto")
        self.entry_prezzo.pack(pady=10)

        # Pulsante per aggiungere corsi
        self.aggiungi_corsi_button = ctk.CTkButton(master, text="Aggiungi Corsi", command=self.aggiungi_corsi)
        self.aggiungi_corsi_button.pack(pady=20)

        # Pulsante per aggiungere il pacchetto
        self.submit_button = ctk.CTkButton(master, text="Aggiungi Pacchetto", command=self.submit_pacchetto)
        self.submit_button.pack(pady=20)

    def aggiungi_corsi(self):
        # Logica per aggiungere corsi al pacchetto (potresti voler aprire un'altra finestra per la selezione dei corsi)
        print("Aggiungi corsi")
        messagebox.showinfo("Aggiungi Corsi", "Qui verranno aggiunti i corsi")
        p = []
        self.pachetto_controller.corsi_selezionati_callback(self, p)

    def submit_pacchetto(self):
        # Prendi i valori inseriti
        nome_pacchetto = self.entry_nome.get()
        prezzo_pacchetto = self.entry_prezzo.get()

        if not nome_pacchetto or not prezzo_pacchetto:
            messagebox.showwarning("Errore", "Compila tutti i campi")
            return

        try:
            prezzo = float(prezzo_pacchetto)
        except ValueError:
            messagebox.showerror("Errore", "Il prezzo deve essere un numero valido")
            return

        # Chiama la funzione di callback per salvare il pacchetto (es. salvarlo nel database)
        self.aggiungi_pacchetto_callback(nome_pacchetto, prezzo)
        messagebox.showinfo("Successo", f"Pacchetto '{nome_pacchetto}' aggiunto con successo!")
        self.master.destroy()  # Chiudi la finestra dopo aver aggiunto il pacchetto