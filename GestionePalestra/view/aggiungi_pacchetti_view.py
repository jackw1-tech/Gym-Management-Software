import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.controller.pacchetto_controller import pacchetto_controller


class AggiungiPacchettoView:
    def __init__(self, master, aggiungi_pacchetto_callback, corsi_selezionati, home_callback):
        self.master = master
        self.master.title("Aggiungi Pacchetto di Corsi")
        self.master.geometry("700x600")
        self.aggiungi_pacchetto_callback = aggiungi_pacchetto_callback
        self.pachetto_controller = pacchetto_controller(self)
        self.corsi_sel = corsi_selezionati
        self.home_callback = home_callback

        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

       
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Pacchetto", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

      
        self.label_nome = ctk.CTkLabel(master, text="Nome Pacchetto:", font=ctk.CTkFont(size=14))
        self.label_nome.pack(pady=10)
        self.entry_nome = ctk.CTkEntry(master, placeholder_text="Inserisci nome pacchetto")
        self.entry_nome.pack(pady=10)

       
        self.label_prezzo = ctk.CTkLabel(master, text="Prezzo Pacchetto (€):", font=ctk.CTkFont(size=14))
        self.label_prezzo.pack(pady=10)
        self.entry_prezzo = ctk.CTkEntry(master, placeholder_text="Inserisci prezzo pacchetto")
        self.entry_prezzo.pack(pady=10)

    
        self.corsi_selezionati_frame = ctk.CTkFrame(master)
        self.corsi_selezionati_frame.pack(fill="both", expand=True, padx=20, pady=10)

      
        self.mostra_corsi_selezionati(corsi_selezionati)

        
        self.aggiungi_corsi_button = ctk.CTkButton(master, text="Aggiungi corsi al pacchetto", command=self.aggiungi_corsi)
        self.aggiungi_corsi_button.pack(pady=10)
       
        self.submit_button = ctk.CTkButton(master, text="Aggiungi Pacchetto", command=self.submit_pacchetto)
        self.submit_button.pack(pady=10)
        self.center_window()
        self.back_button = ctk.CTkButton(master, text="Indietro", command=self.go_back)
        self.back_button.pack(pady=10)

    def center_window(self):
       
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

 
        window_width = 700
        window_height = 600

     
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

      
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def mostra_corsi_selezionati(self, corsi_selezionati):
  
        for widget in self.corsi_selezionati_frame.winfo_children():
            widget.destroy()

   
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
        messagebox.showinfo("Successo", "Pacchetto aggiunto con successo!")
        self.master.destroy()
        self.home_callback()
        
    
    def go_back(self):
        self.master.destroy()
        self.home_callback() 