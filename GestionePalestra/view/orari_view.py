import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.model.sistema import Sistema

class OrariView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Orari Palestra")
        self.master.geometry("400x600")
        ctk.set_appearance_mode("dark")

        
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Orario Palestra", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)
        
     
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=380, height=400)
        self.scrollable_frame.pack(pady=10)

        
        self.entries = {}
        giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
        
     
        orari_esistenti = Sistema.get_orari_esistenti()
        
        
        for giorno in giorni:
            label = ctk.CTkLabel(self.scrollable_frame, text=f"{giorno}: Orario Apertura - Orario Chiusura")
            label.pack(pady=5)

            apertura_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Apertura (es. 08:00)")
            chiusura_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Chiusura (es. 20:00)")
            
           
            if orari_esistenti and giorno in orari_esistenti:
                apertura, chiusura = orari_esistenti[giorno].split('-')
                apertura_entry.insert(0, apertura.strip())
                chiusura_entry.insert(0, chiusura.strip())
            
            apertura_entry.pack(pady=5)
            chiusura_entry.pack(pady=5)

            
            self.entries[giorno] = (apertura_entry, chiusura_entry)
        
 
        self.button_aggiungi = ctk.CTkButton(master, text="Aggiungi Orario", command=self.aggiungi_orario_callback)
        self.button_aggiungi.pack(pady=20)

    def aggiungi_orario_callback(self):
    
        orario_settimanale = {}
        
        for giorno, (apertura_entry, chiusura_entry) in self.entries.items():
            orario_apertura = apertura_entry.get()
            orario_chiusura = chiusura_entry.get()

      
            if not orario_apertura or not orario_chiusura:
                messagebox.showwarning("Campi Mancanti", f"Per favore, compila tutti i campi per {giorno}.")
                return
            

            orario_settimanale[giorno] = f"{orario_apertura}-{orario_chiusura}"
        

        Sistema.aggiungi_orario(orario_settimanale)

        self.master.destroy()
