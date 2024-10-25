import customtkinter as ctk
from tkinter import messagebox

class AggiungiCorsiView:
    def __init__(self, master, corsi_disponibili, corsi_selezionati_callback):
        self.master = master
        self.master.title("Aggiungi Corsi al Pacchetto")
        self.master.geometry("500x500")
        self.corsi_disponibili = corsi_disponibili
        self.corsi_selezionati = []  # Corsi aggiunti al pacchetto
        self.corsi_selezionati_callback = corsi_selezionati_callback

        # Imposta il tema e i colori
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Titolo della schermata
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Corsi al Pacchetto", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)

        # Frame per visualizzare i corsi disponibili
        self.corsi_frame = ctk.CTkFrame(master)
        self.corsi_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Mostra i corsi disponibili
        self.display_corsi_disponibili()

        # Pulsante per creare un nuovo corso
        self.crea_corso_button = ctk.CTkButton(master, text="Crea Corso", command=self.crea_corso)
        self.crea_corso_button.pack(pady=10)

        # Pulsante per confermare i corsi selezionati
        self.conferma_button = ctk.CTkButton(master, text="Conferma Corsi Selezionati", command=self.conferma_corsi)
        self.conferma_button.pack(pady=10)

    def display_corsi_disponibili(self):
        for index, corso in enumerate(self.corsi_disponibili):
            label_corso = ctk.CTkLabel(self.corsi_frame, text=corso['nome'], font=ctk.CTkFont(size=14))
            label_corso.grid(row=index, column=0, padx=10, pady=10, sticky="w")

            button_add = ctk.CTkButton(self.corsi_frame, text="+", width=30, command=lambda c=corso: self.aggiungi_corso(c))
            button_add.grid(row=index, column=1, padx=5, pady=10)

            button_remove = ctk.CTkButton(self.corsi_frame, text="-", width=30, command=lambda c=corso: self.rimuovi_corso(c))
            button_remove.grid(row=index, column=2, padx=5, pady=10)

    def aggiungi_corso(self, corso):
        if corso not in self.corsi_selezionati:
            self.corsi_selezionati.append(corso)
            messagebox.showinfo("Aggiunto", f"Corso {corso['nome']} aggiunto al pacchetto")
        else:
            messagebox.showwarning("Attenzione", f"Corso {corso['nome']} è già stato aggiunto")

    def rimuovi_corso(self, corso):
        if corso in self.corsi_selezionati:
            self.corsi_selezionati.remove(corso)
            messagebox.showinfo("Rimosso", f"Corso {corso['nome']} rimosso dal pacchetto")
        else:
            messagebox.showwarning("Attenzione", f"Corso {corso['nome']} non è stato selezionato")

    def crea_corso(self):
        # Logica per creare un nuovo corso (puoi aprire un'altra finestra per inserire i dettagli del corso)
        print("Creazione di un nuovo corso")
        messagebox.showinfo("Crea Corso", "Qui verrà creato un nuovo corso")

    def conferma_corsi(self):
        # Restituisce i corsi selezionati al callback
        self.corsi_selezionati_callback(self.corsi_selezionati)
        self.master.destroy()