import customtkinter as ctk
from GestionePalestra.view.orari_pt import OrariVisualizzazione
from GestionePalestra.view.orari_view import OrariView

class PTView:
    def __init__(self, master, pt):
        self.master = master
        self.master.title("Gestione Palestra - Dashboard")
        self.master.geometry("700x600")
        self.pt = pt

  
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue") 

      
        self.label_title = ctk.CTkLabel(master, text=f"Dashboard di {pt.get_nome()} {pt.get_cognome()} ", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

       

        self.button_clienti = ctk.CTkButton(master, text="Clienti", state="disabled", fg_color="gray")
        self.button_clienti.pack(pady=10)
        
        self.button_clienti = ctk.CTkButton(master, text="Corsi", state="disabled", fg_color="gray")
        self.button_clienti.pack(pady=10)
        

        self.button_palestra = ctk.CTkButton(master, text="Palestra", command=self.open_palestra)
        self.button_palestra.pack(pady=10)
        
        self.center_window()

    def center_window(self):
     
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

  
        window_width = 700
        window_height = 600

     
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

   
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def open_palestra(self):
        from GestionePersonale.view.sezione_palestra_pt_view import Sezione_palestra_pt_View
        self.master.destroy()
        orari_finestra = ctk.CTk()
        Sezione_palestra_pt_View(orari_finestra, self.pt)
        orari_finestra.mainloop()