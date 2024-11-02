import customtkinter as ctk
from tkinter import messagebox

class ModificaPacchettoView:
    def __init__(self, master, corsi_disponibili, corsi_selezionati, corsi_selezionati_callback, nome_pacchetto, prezzo_pacchetto,id_pacchetto, torna_indietro):
        self.master = master
        self.master.title("Modifica Pacchetto Corsi")
        self.master.geometry("700x600")
        self.corsi_disponibili = corsi_disponibili
        self.corsi_selezionati = corsi_selezionati 
        self.corsi_selezionati_callback = corsi_selezionati_callback
        self.id_pacchetto = id_pacchetto
        self.back = torna_indietro
     
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

       
        self.label_title = ctk.CTkLabel(master, text="Modifica Pacchetto Corsi", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)

       
        self.scrollable_frame = ctk.CTkScrollableFrame(master)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.label_nome = ctk.CTkLabel(self.scrollable_frame, text="Nome Pacchetto:", font=ctk.CTkFont(size=14))
        self.label_nome.pack(pady=(10, 0))
        self.entry_nome = ctk.CTkEntry(self.scrollable_frame, width=300)
        self.entry_nome.pack(pady=(0, 10))
        self.entry_nome.insert(0, nome_pacchetto) 

      
        self.label_prezzo = ctk.CTkLabel(self.scrollable_frame, text="Prezzo Pacchetto:", font=ctk.CTkFont(size=14))
        self.label_prezzo.pack(pady=(10, 0))
        self.entry_prezzo = ctk.CTkEntry(self.scrollable_frame, width=300)
        self.entry_prezzo.pack(pady=(0, 10))
        self.entry_prezzo.insert(0, str(prezzo_pacchetto)) 

     
        self.label_selezionati = ctk.CTkLabel(self.scrollable_frame, text="Corsi Selezionati", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_selezionati.pack(pady=(10, 0))

        self.display_corsi_selezionati()

     
        self.separator1 = ctk.CTkFrame(self.scrollable_frame, height=2, width=700)
        self.separator1.pack(pady=10)


        self.label_disponibili = ctk.CTkLabel(self.scrollable_frame, text="Corsi Disponibili", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_disponibili.pack(pady=(10, 0))

        self.display_corsi_disponibili()

      
        self.conferma_button = ctk.CTkButton(master, text="Conferma Modifiche", command=self.conferma_modifiche)
        self.conferma_button.pack(pady=10)

      
        self.torna_indietro_button = ctk.CTkButton(master, text="Torna Indietro", command= self.tasto_indietro)
        self.torna_indietro_button.pack(pady=10)

        self.center_window()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 700
        window_height = 600
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")
    def tasto_indietro(self):
        self.master.destroy
        self.back()
        
        
    def display_corsi_selezionati(self):
        for index, corso in enumerate(self.corsi_selezionati):
            frame_corso = ctk.CTkFrame(self.scrollable_frame)
            frame_corso.pack(fill="x", padx=10, pady=5)

            label_corso = ctk.CTkLabel(frame_corso, text=f"{corso['nome']}", font=ctk.CTkFont(size=14))
            label_corso.pack(side="left", padx=(0, 10))

            button_remove = ctk.CTkButton(frame_corso, text="-", command=lambda c=corso: self.rimuovi_corso(c))
            button_remove.pack(side="right")

    def display_corsi_disponibili(self):
        for index, corso in enumerate(self.corsi_disponibili):
            frame_corso = ctk.CTkFrame(self.scrollable_frame)
            frame_corso.pack(fill="x", padx=10, pady=5)

            label_corso = ctk.CTkLabel(frame_corso, text=f"{corso['nome']}", font=ctk.CTkFont(size=14))
            label_corso.pack(side="left", padx=(0, 10))

            button_add = ctk.CTkButton(frame_corso, text="+", command=lambda c=corso: self.aggiungi_corso(c))
            button_add.pack(side="right")

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

   

    def display_nome_pacchetto(self):
        self.label_nome.pack(pady=(10, 0))
        self.entry_nome.pack(pady=(0, 10))

    def display_prezzo_pacchetto(self):
        self.label_prezzo.pack(pady=(10, 0))
        self.entry_prezzo.pack(pady=(0, 10))

    def conferma_modifiche(self):
        nome_nuovo = self.entry_nome.get()
        prezzo_nuovo = self.entry_prezzo.get()
        

        try:
            prezzo_nuovo_float = float(prezzo_nuovo)
            messagebox.showinfo("Aggiornamento Completato", "Il pacchetto è stato aggiornato")
            self.master.destroy()
            self.corsi_selezionati_callback(self.id_pacchetto, self.corsi_selezionati, nome_nuovo, prezzo_nuovo_float, ) 
        
        except ValueError:
            messagebox.showerror("Errore", "Il prezzo deve essere un numero valido")

