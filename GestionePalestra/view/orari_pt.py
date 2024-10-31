import customtkinter as ctk
from GestionePalestra.model.sistema import Sistema
import os
from dotenv import load_dotenv


load_dotenv()
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


# Classe per la schermata di visualizzazione degli orari (solo lettura)
class OrariVisualizzazione:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizzazione Orari Palestra")
        self.master.geometry("400x400")
        ctk.set_appearance_mode("dark")

        # Titolo della schermata
        self.label_title = ctk.CTkLabel(master, text="Orari Palestra", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)
        
        # Cornice scorrevole per mostrare gli orari
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=380, height=300)
        self.scrollable_frame.pack(pady=10)

        # Ottieni gli orari settimanali dal sistema
        sistema = Sistema(cred_path)
        orario_settimanale = sistema.get_orario_settimanale()
        
        # Visualizza gli orari, se disponibili
        if orario_settimanale:
            for giorno, orario in orario_settimanale.items():
                label = ctk.CTkLabel(self.scrollable_frame, text=f"{giorno}: {orario}", anchor="w")
                label.pack(fill='x', padx=10, pady=5)
        else:
            no_data_label = ctk.CTkLabel(self.scrollable_frame, text="Nessun orario disponibile")
            no_data_label.pack(pady=10)

# Avvia l'applicazione
if __name__ == "__main__":
    root = ctk.CTk()
    app = OrariVisualizzazione(root)
    root.mainloop()