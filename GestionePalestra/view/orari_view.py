import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.model.sistema import Sistema


# Classe per la schermata "Orari"
class OrariView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Orari Palestra")
        self.master.geometry("400x600")
        ctk.set_appearance_mode("dark")

        # Titolo della schermata
        self.label_title = ctk.CTkLabel(master, text="Aggiungi Orario Palestra", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)
        
        # Cornice scorrevole
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=380, height=400)
        self.scrollable_frame.pack(pady=10)

        # Dizionario per memorizzare i campi degli orari
        self.entries = {}
        giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
        
        # Creazione dei campi per ciascun giorno nella cornice scorrevole
        for giorno in giorni:
            label = ctk.CTkLabel(self.scrollable_frame, text=f"{giorno}: Orario Apertura - Orario Chiusura")
            label.pack(pady=5)

            apertura_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Apertura (es. 08:00)")
            apertura_entry.pack(pady=5)
            chiusura_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Chiusura (es. 20:00)")
            chiusura_entry.pack(pady=5)

            # Salva le entry nel dizionario per accedervi successivamente
            self.entries[giorno] = (apertura_entry, chiusura_entry)
        
        # Pulsante per aggiungere l'orario
        self.button_aggiungi = ctk.CTkButton(master, text="Aggiungi Orario", command=self.aggiungi_orario_callback)
        self.button_aggiungi.pack(pady=20)
    
    def aggiungi_orario_callback(self):
        # Crea un dizionario per gli orari settimanali
        orario_settimanale = {}
        
        for giorno, (apertura_entry, chiusura_entry) in self.entries.items():
            orario_apertura = apertura_entry.get()
            orario_chiusura = chiusura_entry.get()

            # Verifica che entrambi i campi per ogni giorno siano riempiti
            if not orario_apertura or not orario_chiusura:
                messagebox.showwarning("Campi Mancanti", f"Per favore, compila tutti i campi per {giorno}.")
                return
            
            # Formatta l'orario per il giorno
            orario_settimanale[giorno] = f"{orario_apertura}-{orario_chiusura}"
        
        # Chiama la funzione per aggiungere l'orario
        Sistema.aggiungi_orario(orario_settimanale)

# Avvia l'applicazione
if __name__ == "__main__":
    root = ctk.CTk()
    app = OrariView(root)
    root.mainloop()


