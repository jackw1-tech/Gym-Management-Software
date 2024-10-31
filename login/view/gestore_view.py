import customtkinter as ctk
from GestionePersonale.view.personale_view import PersonaleView
from GestionePalestra.view.palestra_view import PalestraView

class MainView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Palestra - Dashboard")
        self.master.geometry("700x600")

        
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("blue")

        
        self.label_title = ctk.CTkLabel(master, text="Dashboard", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        
        self.button_clienti = ctk.CTkButton(master, text="Clienti", state="disabled", fg_color="gray")
        self.button_clienti.pack(pady=10)

        self.button_personale = ctk.CTkButton(master, text="Personale", command=self.open_personale)
        self.button_personale.pack(pady=10)

        self.button_palestra = ctk.CTkButton(master, text="Palestra", command=self.open_palestra)
        self.button_palestra.pack(pady=10)

        self.button_contabilita = ctk.CTkButton(master, text="Contabilità", state="disabled", fg_color="gray")
        self.button_contabilita.pack(pady=10)

        
        self.center_window()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

       
        window_width = 700
        window_height = 600

    
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

  
   

    def open_personale(self):
        self.master.destroy()
        main_window = ctk.CTk()
        PersonaleView(main_window, home_callback=self.go_back_home)
        main_window.mainloop()

    def open_palestra(self):
        print("Apertura schermata Palestra")
        self.master.destroy()
        main_window = ctk.CTk()
        PalestraView(main_window, home_callback=self.go_back_home) 
        main_window.mainloop()

 

    def go_back_home(self):
        home_window = ctk.CTk()
        MainView(home_window)
        home_window.mainloop()
