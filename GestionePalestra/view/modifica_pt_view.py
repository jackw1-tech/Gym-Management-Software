from datetime import datetime
from tkinter import messagebox
import customtkinter as ctk
from GestionePersonale.controller.pt_controller import PTController
from GestionePersonale.model.pt import PT

class ModificaPTView:
    def __init__(self, master, home_callback, trainer_data):
        self.master = master
        self.master.title("Modifica Personal Trainer")
        self.master.geometry("700x600")
        self.controller = PTController(self)
        self.trainer_data = trainer_data  
        
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("blue")  

    
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=550)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        
        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Modifica Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        
        self.label_nome = ctk.CTkLabel(self.scrollable_frame, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il nome")
        self.entry_nome.insert(0, trainer_data['nome'])
        self.entry_nome.pack(pady=5)

        self.label_cognome = ctk.CTkLabel(self.scrollable_frame, text="Cognome:")
        self.label_cognome.pack(pady=5)
        self.entry_cognome = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci il cognome")
        self.entry_cognome.insert(0, trainer_data['cognome'])  
        self.entry_cognome.pack(pady=5)

        self.label_stipendio = ctk.CTkLabel(self.scrollable_frame, text="Stipendio:")
        self.label_stipendio.pack(pady=5)
        self.entry_stipendio = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci lo stipendio")
        self.entry_stipendio.insert(0, trainer_data['stipendio']) 
        self.entry_stipendio.pack(pady=5)

        self.label_username = ctk.CTkLabel(self.scrollable_frame, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci lo username")
        self.entry_username.insert(0, trainer_data['username'])
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.scrollable_frame, text="Password (obbligatoria):")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la password", show="*")
        
        self.entry_password.pack(pady=5)

        
        self.label_stato = ctk.CTkLabel(self.scrollable_frame, text="Stato:")
        self.label_stato.pack(pady=5)

     
        stati = ["Inattivo", "In ferie", "Disponibile"]
        self.optionmenu_stato = ctk.CTkOptionMenu(self.scrollable_frame, values=stati, command=self.on_stato_change)
        self.optionmenu_stato.set(trainer_data['stato']) 
        self.optionmenu_stato.pack(pady=5)

        
        self.label_data_inizio = ctk.CTkLabel(self.scrollable_frame, text="Data inizio ferie (DD/MM/YYYY):")
        self.entry_data_inizio = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la data di inizio")
        self.entry_data_inizio.insert(0, trainer_data['data_inizio']) 
        
        self.label_data_fine = ctk.CTkLabel(self.scrollable_frame, text="Data fine ferie (DD/MM/YYYY):")
        self.entry_data_fine = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Inserisci la data di fine")
        self.entry_data_fine.insert(0, trainer_data['data_fine']) 

        if trainer_data['stato'] == "In ferie":
            self.mostra_campi_ferie()

    
        self.button_salva = ctk.CTkButton(self.scrollable_frame, text="Salva Modifiche", command=lambda: self.salva_modifiche_pt(home_callback))
        self.button_salva.pack(pady=10)


        self.button_back_home = ctk.CTkButton(self.scrollable_frame, text="Torna indietro", command=lambda: self.torna_alla_home(home_callback))
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

    def on_stato_change(self, stato_selezionato):
      
       if stato_selezionato == "In ferie":
           self.mostra_campi_ferie()
       else:
           self.nascondi_campi_ferie()

    def mostra_campi_ferie(self):
       self.label_data_inizio.pack(pady=5)
       self.entry_data_inizio.pack(pady=5)
       self.label_data_fine.pack(pady=5)
       self.entry_data_fine.pack(pady=5)

    def nascondi_campi_ferie(self):
       self.label_data_inizio.pack_forget()
       self.entry_data_inizio.pack_forget()
       self.label_data_fine.pack_forget()
       self.entry_data_fine.pack_forget()
       
    def torna_alla_home(self, funzione):
        self.master.destroy() 
        funzione() 

    def salva_modifiche_pt(self, funzione):
       nome = self.entry_nome.get()
       cognome = self.entry_cognome.get()
       stipendio = self.entry_stipendio.get()
       username = self.entry_username.get()
       password = self.entry_password.get()
      
       if not password:  
           messagebox.showinfo("Errore", "Password Obbligatoria")
           return

       stato = self.optionmenu_stato.get()

       data_inizio = self.entry_data_inizio.get()
       if data_inizio:
        try:
               
                datetime.strptime(data_inizio, "%d/%m/%Y")
            
        except ValueError:
                
                messagebox.showerror("Errore", "Inserisci la data di inizio ferie nel formato DD/MM/YYYY.")
            
       data_fine = self.entry_data_fine.get()
       if data_fine: 
        try:
                
                datetime.strptime(data_fine, "%d/%m/%Y")
            
        except ValueError:
               
                messagebox.showerror("Errore", "Inserisci la data di fine ferie nel formato DD/MM/YYYY.")

       
       if stato == "In ferie":
           data_inizio = self.entry_data_inizio.get()
           data_fine = self.entry_data_fine.get()
       else:
           data_inizio = None
           data_fine = None

       
       PT.aggiorna_dati(self,
                        id_document=self.trainer_data['id'], 
                        nome=nome,
                        cognome=cognome,
                        stipendio=stipendio,
                        username=username,
                        password=password,
                        stato=stato,
                        data_inizio=data_inizio,
                        data_fine=data_fine)
       self.master.destroy() 
       funzione()  
