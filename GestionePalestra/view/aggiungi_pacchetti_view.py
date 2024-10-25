import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.controller.pacchetto_controller import pacchetto_controller
from GestionePalestra.view.aggiungi_corsi_view import AggiungiCorsiView

class AggiungiPacchettoView:
    def __init__(self, master, aggiungi_pacchetto_callback, corsi_selezionati):
        self.master = master
        self.master.title("Aggiungi Pacchetto di Corsi")
        self.master.geometry("400x400")
        self.aggiungi_pacchetto_callback = aggiungi_pacchetto_callback
        self.pachetto_controller = pacchetto_controller(self)
        self.corsi_sel = corsi_selezionati

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

        # Frame per visualizzare i corsi selezionati
        self.corsi_selezionati_frame = ctk.CTkFrame(master)
        self.corsi_selezionati_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Mostra i corsi selezionati
        self.mostra_corsi_selezionati(corsi_selezionati)

        # Pulsante per aggiungere corsi
        self.aggiungi_corsi_button = ctk.CTkButton(master, text="Aggiungi Corsi", command=self.aggiungi_corsi)
        self.aggiungi_corsi_button.pack(pady=20)

        # Pulsante per aggiungere il pacchetto
        self.submit_button = ctk.CTkButton(master, text="Aggiungi Pacchetto", command=self.submit_pacchetto)
        self.submit_button.pack(pady=20)

    def mostra_corsi_selezionati(self, corsi_selezionati):
        # Pulisci il frame esistente
        for widget in self.corsi_selezionati_frame.winfo_children():
            widget.destroy()

        # Mostra i corsi selezionati
        if not corsi_selezionati:
            label_no_courses = ctk.CTkLabel(self.corsi_selezionati_frame, text="Nessun corso selezionato.", font=ctk.CTkFont(size=14))
            label_no_courses.pack(pady=10)
            return

        for corso in corsi_selezionati:
            label_corso = ctk.CTkLabel(self.corsi_selezionati_frame, text=corso['nome'], font=ctk.CTkFont(size=14))
            label_corso.pack(pady=5)

    def aggiungi_corsi(self):
        self.master.destroy()
        self.pachetto_controller.aggiungi_corso_view()
        
    def submit_pacchetto(self):
        nome_pacchetto = self.entry_nome.get()
        prezzo_pacchetto = self.entry_prezzo.get()
      
        self.pachetto_controller.crea_pacchetto(nome_pacchetto,prezzo_pacchetto,self.corsi_sel)
        
        messagebox.showinfo("Successo", f"Pacchetto '{nome_pacchetto}' aggiunto con successo!")
        self.master.destroy() 