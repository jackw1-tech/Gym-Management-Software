import customtkinter as ctk
from tkinter import messagebox

class AggiungiCorsiView:
    def __init__(self, master, corsi_disponibili, corsi_selezionati_callback):
        self.master = master
        self.master.title("Aggiungi Corsi al Pacchetto")
        self.master.geometry("700x600")
        self.corsi_disponibili = corsi_disponibili
        self.corsi_selezionati = [] 
        self.corsi_selezionati_callback = corsi_selezionati_callback

       
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

      
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Corsi al Pacchetto", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)

       
        self.scrollable_frame = ctk.CTkScrollableFrame(master)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=10)

        
        self.display_corsi_disponibili()

      
        self.conferma_button = ctk.CTkButton(master, text="Conferma Corsi Selezionati", command=self.conferma_corsi)
        self.conferma_button.pack(pady=10)
        
        self.torna_indietro_button = ctk.CTkButton(master, text="Torna Indietro", command=self.conferma_corsi)
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

    def display_corsi_disponibili(self):
        for index, corso in enumerate(self.corsi_disponibili):
            label_corso = ctk.CTkLabel(self.scrollable_frame, text=corso['nome'], font=ctk.CTkFont(size=14))
            label_corso.grid(row=index, column=0, padx=10, pady=10, sticky="w")
            button_add = ctk.CTkButton(self.scrollable_frame, text="+", width=30, command=lambda c=corso: self.aggiungi_corso(c))
            button_add.grid(row=index, column=1, padx=5, pady=10)

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

    def conferma_corsi(self):
        self.master.destroy()
        self.corsi_selezionati_callback(self.corsi_selezionati)

   