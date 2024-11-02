import customtkinter as ctk

class PacchettoDetailsView:
    def __init__(self, master, lista_corsi, nome, prezzo):
        self.master = master
        self.master.title("Dettagli del Pacchetto")
        self.master.geometry("500x400")

       
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

     
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=550)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)


        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Dettagli del pacchetto", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        label_nome_corso = ctk.CTkLabel(self.scrollable_frame, text=f"Nome pacchetto: {nome}", font=ctk.CTkFont(size=16))
        label_nome_corso.pack(pady=10)
        
        label_prezzo_corso = ctk.CTkLabel(self.scrollable_frame, text=f"Prezzo pacchetto: {prezzo}", font=ctk.CTkFont(size=16))
        label_prezzo_corso.pack(pady=10)
        
        separator = ctk.CTkLabel(self.scrollable_frame, text="-" * 50)
        separator.pack(pady=10)
        
        label_scritta = ctk.CTkLabel(self.scrollable_frame, text="Lista Corsi: ", font=ctk.CTkFont(size=16))
        label_scritta.pack(pady=15)
        
        for corso in lista_corsi:
           
            label_nome = ctk.CTkLabel(self.scrollable_frame, text=f"Nome: {corso['nome']}", font=ctk.CTkFont(size=16))
            label_nome.pack(pady=5)

          
            label_prezzo = ctk.CTkLabel(self.scrollable_frame, text=f"Descrizione: {corso['descrizione']} ", font=ctk.CTkFont(size=16))
            label_prezzo.pack(pady=5)

        
            separator = ctk.CTkLabel(self.scrollable_frame, text="-" * 30)
            separator.pack(pady=10)

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = 500
        window_height = 400

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")



