import customtkinter as ctk
from GestionePalestra.view.orari_pt import OrariVisualizzazione
from GestionePalestra.view.orari_view import OrariView

class Sezione_palestra_pt_View:
    def __init__(self, master, pt):
        self.master = master
        self.master.title("Sezione Palestra - PT ")
        self.master.geometry("700x600")
        self.pt = pt
       
       
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")  

       
        self.label_title = ctk.CTkLabel(master, text=f"Sezione palestra di {pt.get_nome()} {pt.get_cognome()} ", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

      
        self.button_stipendio = ctk.CTkButton(master, text="Visualizza Stipendio", command=self.open_stipendio)
        self.button_stipendio.pack(pady=10)
        
        self.button_palestra = ctk.CTkButton(master, text="Visualizza Orari", command=self.open_orari)
        self.button_palestra.pack(pady=10)
        
        self.button_palestra = ctk.CTkButton(master, text="Torna indietro", command=self.back)
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


  
    def open_stipendio(self):
        stipendio_value = (self.pt).get_stipendio() 
        stipendio_finestra = ctk.CTkToplevel(self.master) 
        stipendio_finestra.title("Visualizza Stipendio")
        
  
        stipendio_label = ctk.CTkLabel(stipendio_finestra, text=f" Stipendio: {stipendio_value} ", font=ctk.CTkFont(size=18, weight="bold"))
        stipendio_label.pack(pady=20)

       

    def back(self):
        self.master.destroy()
        from GestionePersonale.view.pt_view import PTView
        main_window = ctk.CTk() 
        main_window.title("Dashboard PT")
        PTView(main_window, self.pt)

    def open_orari(self):
        orari_finestra = ctk.CTk()
        OrariVisualizzazione(orari_finestra)
        orari_finestra.mainloop()