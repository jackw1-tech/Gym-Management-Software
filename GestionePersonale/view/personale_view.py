import customtkinter as ctk
from GestionePersonale.view.aggiungi_pt_view import AggiungiPTView
from GestionePersonale.controller.pt_controller import PTController
class PersonaleView:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Gestione Personal Trainer")
        self.master.geometry("700x600")
        self.controller = PTController(self)

        
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("blue") 

  
        self.label_title = ctk.CTkLabel(master, text="Gestione Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

       
        self.button_add_pt = ctk.CTkButton(master, text="Aggiungi PT", command=lambda: self.add_pt(home_callback))
        self.button_add_pt.pack(pady=10)

        self.button_find_pt = ctk.CTkButton(master, text="Trova PT", command= self.find_pt)
        self.button_find_pt.pack(pady=10)

      
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


    def add_pt(self,funzione):
        print("Apertura schermata per aggiungere PT")
        self.master.destroy() 
        main_window = ctk.CTk() 
        AggiungiPTView(main_window, home_callback= funzione) 
        main_window.mainloop()

    def find_pt(self):
        self.master.destroy()
        self.controller.get_view_trova_pt()
        
        

        