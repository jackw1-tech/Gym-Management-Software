import customtkinter as ctk
from GestionePalestra.model.sistema import Sistema
import os
from dotenv import load_dotenv


class OrariVisualizzazione:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizzazione Orari Palestra")
        self.master.geometry("400x400")
        ctk.set_appearance_mode("dark")

    
        self.label_title = ctk.CTkLabel(master, text="Orari Palestra", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)
        
      
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=380, height=300)
        self.scrollable_frame.pack(pady=10)

     
        orario_settimanale = Sistema.get_orari_esistenti()
        giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

        if orario_settimanale:
            for giorno in giorni:  
                orario = orario_settimanale.get(giorno, "Nessun orario disponibile")
                label = ctk.CTkLabel(self.scrollable_frame, text=f"{giorno}: {orario}", anchor="w")
                label.pack(fill='x', padx=10, pady=5)

       
        else:
            no_data_label = ctk.CTkLabel(self.scrollable_frame, text="Nessun orario disponibile")
            no_data_label.pack(pady=10)

