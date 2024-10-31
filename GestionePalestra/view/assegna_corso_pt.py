import customtkinter as ctk
from tkinter import messagebox

from GestionePersonale.controller.pt_controller import PTController

class AssegnaCorsiView:
    def __init__(self, master, pt_id, corsi_attuali, corsi_disponibili, assegna_corso_callback, back_callback):
        self.master = master
        self.master.title("Assegna Corsi al PT")
        self.master.geometry("700x600")
        self.pt_id = pt_id
        self.corsi_attuali = corsi_attuali
        self.corsi_disponibili = corsi_disponibili
        self.assegna_corso_callback = assegna_corso_callback
        self.back_callback = back_callback
        self.controller = PTController(self)

        
        # Imposta il tema e i colori
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=360)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)
        # Titolo della schermata
        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Assegna Corsi al PT", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Campo di ricerca
        self.label_search = ctk.CTkLabel(self.scrollable_frame, text="Cerca Corsi:", font=ctk.CTkFont(size=14))
        self.label_search.pack(pady=10)
        self.entry_search = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci nome corso")
        self.entry_search.pack(pady=10)

        # Pulsante Cerca
        self.search_button = ctk.CTkButton(self.scrollable_frame, text="Cerca", command=self.cerca_corsi)
        self.search_button.pack(pady=10)

        # Pulsante Torna Indietro
        self.back_button = ctk.CTkButton(self.scrollable_frame, text="Torna Indietro", command=self.torna_indietro)
        self.back_button.pack(pady=10)

        self.label_disponibili = ctk.CTkLabel(self.scrollable_frame, text="Corsi disponibili:", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_disponibili.pack(pady=10)
        # Frame per corsi disponibili
        self.corsi_disponibili_frame = ctk.CTkFrame(self.scrollable_frame)
        self.corsi_disponibili_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.mostra_corsi_disponibili(corsi_disponibili)

        # Etichetta per i corsi già assegnati
        self.label_assegnati = ctk.CTkLabel(self.scrollable_frame, text="Corsi già assegnati:", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_assegnati.pack(pady=10)

        # Frame per corsi assegnati
        self.corsi_asportati_frame = ctk.CTkFrame(self.scrollable_frame)
        self.corsi_asportati_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.mostra_corsi_asportati(corsi_attuali)
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


    def torna_indietro(self):
        self.master.destroy() 
        self.back_callback(self)
        
    def mostra_corsi_disponibili(self, corsi):
        # Pulisci il frame esistente
        for widget in self.corsi_disponibili_frame.winfo_children():
            widget.destroy()

        # Mostra i corsi disponibili
        for corso in corsi:
            frame = ctk.CTkFrame(self.corsi_disponibili_frame)
            frame.pack(fill="x", pady=5)

            label_corso = ctk.CTkLabel(frame, text=corso['nome'], font=ctk.CTkFont(size=14))
            label_corso.pack(side="left", padx=(20, 10))  # Aggiunto padding laterale

            button_assegna = ctk.CTkButton(frame, text="+", command=lambda c=corso: self.assegna_corso(c))
            button_assegna.pack(side="right")

    def mostra_corsi_asportati(self, corsi):
        # Pulisci il frame esistente
        for widget in self.corsi_asportati_frame.winfo_children():
            widget.destroy()

        # Mostra i corsi già assegnati
        for corso in corsi:
            frame = ctk.CTkFrame(self.corsi_asportati_frame)
            frame.pack(fill="x", pady=5)

            label_corso = ctk.CTkLabel(frame, text=corso['nome'], font=ctk.CTkFont(size=14))
            label_corso.pack(side="left", padx=(20, 10))  # Aggiunto padding laterale

            button_rimuovi = ctk.CTkButton(frame, text="-", command=lambda c=corso: self.rimuovi_corso(c))
            button_rimuovi.pack(side="right")

    def assegna_corso(self, corso):
        self.assegna_corso_callback(self, self.pt_id, corso['id'],  "+")
        messagebox.showinfo("Successo", f"Corso '{corso['nome']}' assegnato con successo!")
        self.master.destroy()
        self.controller.assegna_corsi_view(str(self.pt_id))

    def rimuovi_corso(self, corso):
        self.assegna_corso_callback(self, self.pt_id, corso['id'],  "-")
        messagebox.showinfo("Successo", f"Corso '{corso['nome']}' rimosso con successo!")
        self.master.destroy() 
        self.controller.assegna_corsi_view(str(self.pt_id))
        
    def cerca_corsi(self):
        termine = self.entry_search.get().lower()
        corsi_filtrati = [corso for corso in self.corsi_disponibili if termine in corso['nome'].lower()]
        self.mostra_corsi_disponibili(corsi_filtrati)
    
    