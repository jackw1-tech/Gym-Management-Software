import customtkinter as ctk

class CorsoDetailsView:
    def __init__(self, master, lista_pt, nome, descrizione):
        self.master = master
        self.master.title("Dettagli del Corso")
        self.master.geometry("500x400")

        # Imposta il tema scuro e il tema colore blu
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Frame scorrevole per i dettagli dei corsi
        self.scrollable_frame = ctk.CTkScrollableFrame(master, width=580, height=550)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Titolo della pagina
        self.label_title = ctk.CTkLabel(self.scrollable_frame, text="Dettagli del Corso", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        label_nome_corso = ctk.CTkLabel(self.scrollable_frame, text=f"Nome corso: {nome}", font=ctk.CTkFont(size=16))
        label_nome_corso.pack(pady=10)
        
        label_prezzo_corso = ctk.CTkLabel(self.scrollable_frame, text=f"Descrizione corso: {descrizione}", font=ctk.CTkFont(size=16))
        label_prezzo_corso.pack(pady=10)
        
        separator = ctk.CTkLabel(self.scrollable_frame, text="-" * 50)
        separator.pack(pady=10)
        
        label_scritta = ctk.CTkLabel(self.scrollable_frame, text="Lista Pt: ", font=ctk.CTkFont(size=16))
        label_scritta.pack(pady=15)
        
        
        for index, pt in enumerate(lista_pt):
            # Etichetta per il nome del corso
            label_nome = ctk.CTkLabel(self.scrollable_frame, text=f"Nome: {pt['nome']} {pt['cognome']}", font=ctk.CTkFont(size=16))
            label_nome.pack(pady=5)

            # Separator tra i corsi
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



