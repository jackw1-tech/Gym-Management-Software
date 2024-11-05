from tkinter import messagebox
import customtkinter as ctk
from GestionePersonale.controller.gestore_controller import GestoreController  

class registra_gestore_view:
    def __init__(self, master, home_callback):
        self.master = master
        self.master.title("Registrazione Gestore")
        self.master.geometry("700x600")
        self.controller = GestoreController(self)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
       
        

       
        self.label_title = ctk.CTkLabel(self.master, text="Benvenuto, registrati come gestore", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        
        self.label_nome = ctk.CTkLabel(self.master, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self.master, placeholder_text="Inserisci il nome")
        self.entry_nome.pack(pady=5)

        self.label_cognome = ctk.CTkLabel(self.master, text="Cognome:")
        self.label_cognome.pack(pady=5)
        self.entry_cognome = ctk.CTkEntry(self.master, placeholder_text="Inserisci il cognome")
        self.entry_cognome.pack(pady=5)

    

        self.label_username = ctk.CTkLabel(self.master, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(self.master, placeholder_text="Inserisci lo username")
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.master, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(self.master, placeholder_text="Inserisci la password", show="*")
        self.entry_password.pack(pady=5)

        
        self.button_registra = ctk.CTkButton(self.master, text="Registrati", command=lambda: self.registra_gestore(home_callback))
        self.button_registra.pack(pady=10)

        self.center_window()

    def center_window(self):
       
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

       
        window_width = 700
        window_height = 600

    
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

   
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")


    def registra_gestore(self,funzione):
        nome = self.entry_nome.get()
        cognome = self.entry_cognome.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        if self.controller.crea_gestore(nome,cognome,username,password):
            messagebox.showinfo("Successo", "Registrazione avvenuta con successo")
            funzione()
        else:
            messagebox.showinfo("Errore", "Errore nella registrazione")