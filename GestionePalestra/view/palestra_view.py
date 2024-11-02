import customtkinter as ctk
from GestionePalestra.controller.pacchetto_controller import pacchetto_controller



class PalestraView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Gestione Palestra")
        self.master.geometry("700x600")
        self.controller = pacchetto_controller(self)
    
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("blue")

     
        self.label_title = ctk.CTkLabel(master, text="Gestione Palestra", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

      
        self.button_orari = ctk.CTkButton(master, text="Orari", command=self.visualizza_orari)
        self.button_orari.pack(pady=10)

        self.button_pacchetti = ctk.CTkButton(master, text="Pacchetti", command=self.visualizza_pacchetti)
        self.button_pacchetti.pack(pady=10)

        self.button_corsi = ctk.CTkButton(master, text="Corsi", command=self.visualizza_corsi)
        self.button_corsi.pack(pady=10)

    
        self.button_back_home = ctk.CTkButton(master, text="Torna alla Home", command=lambda: self.torno_alla_home(home_callback))
        self.button_back_home.pack(pady=10)
        self.center_window()

    def center_window(self):
        
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()


        window_width = 700
        window_height = 600

      
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")


    def torno_alla_home(self, funzione):
        self.master.destroy()  
        funzione()


    def visualizza_orari(self):
        from GestionePalestra.view.orari_view import OrariView
        orari_view_window = ctk.CTkToplevel(self.master)  
        orari_view_app = OrariView(orari_view_window)   


    def visualizza_pacchetti(self):
        self.master.destroy()
        nuova_master = ctk.CTk() 
        controller = pacchetto_controller(nuova_master)
        controller.open_course_package_search()
        nuova_master.mainloop()
        
    
    def visualizza_corsi(self):
        from GestionePalestra.controller.corso_controller import corso_controller
        self.master.destroy()
        controller = corso_controller(self)
        controller.sezione_corsi_view()
    