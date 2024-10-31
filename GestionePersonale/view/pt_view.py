import customtkinter as ctk

class PTView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Palestra - Dashboard")
        self.master.geometry("700x600")


       
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue")  

       
        self.label_title = ctk.CTkLabel(master, text="Dashboard", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

      
        self.button_clienti = ctk.CTkButton(master, text="Clienti", command=self.open_clienti)
        self.button_clienti.pack(pady=10)

        self.button_corsi = ctk.CTkButton(master, text="Corsi", command=self.open_corsi)
        self.button_corsi.pack(pady=10)

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


   
    def open_clienti(self):
        print("Apertura schermata Clienti")

    def open_corsi(self):
        print("Apertura schermata Corsi")

    def open_palestra(self):
        print("Apertura schermata Palestra")