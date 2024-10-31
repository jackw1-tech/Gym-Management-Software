import customtkinter as ctk
from tkinter import messagebox

class ModificaCorsoView:
    def __init__(self, master, nome_corso, descrizione_corso, pts_assegnati, pts_assegnati_callback, id_corso, torna_indietro):
        self.master = master
        self.master.title("Modifica Corso")
        self.master.geometry("700x600")
        self.pts_assegnati = pts_assegnati  # PT già assegnati
        self.pts_assegnati_callback = pts_assegnati_callback
        self.id_corso = id_corso
        self.back = torna_indietro

        # Imposta tema e colori
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Titolo schermata
        self.label_title = ctk.CTkLabel(master, text="Modifica Corso", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=20)

        # Frame scorrevole principale
        self.scrollable_frame = ctk.CTkScrollableFrame(master)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Sezione Nome Corso
        self.label_nome = ctk.CTkLabel(self.scrollable_frame, text="Nome Corso:", font=ctk.CTkFont(size=14))
        self.label_nome.pack(pady=(10, 0))
        self.entry_nome = ctk.CTkEntry(self.scrollable_frame, width=300)
        self.entry_nome.pack(pady=(0, 10))
        self.entry_nome.insert(0, nome_corso)

        # Sezione Descrizione Corso
        self.label_descrizione = ctk.CTkLabel(self.scrollable_frame, text="Descrizione Corso:", font=ctk.CTkFont(size=14))
        self.label_descrizione.pack(pady=(10, 0))
        self.entry_descrizione = ctk.CTkEntry(self.scrollable_frame, width=300)
        self.entry_descrizione.pack(pady=(0, 10))
        self.entry_descrizione.insert(0, descrizione_corso)

        # Sezione PT Assegnati
        self.label_pts_assegnati = ctk.CTkLabel(self.scrollable_frame, text="PT Assegnati", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_pts_assegnati.pack(pady=(10, 0))

        self.display_pts_assegnati()

        # Pulsante per confermare le modifiche
        self.conferma_button = ctk.CTkButton(master, text="Conferma Modifiche", command=self.conferma_modifiche)
        self.conferma_button.pack(pady=10)

        # Pulsante per tornare indietro
        self.torna_indietro_button = ctk.CTkButton(master, text="Torna Indietro", command=self.tasto_indietro)
        self.torna_indietro_button.pack(pady=10)

        self.center_window()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 700
        window_height = 600
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def tasto_indietro(self):
        self.master.destroy()
        self.back()

    def display_pts_assegnati(self):
        for pt in self.pts_assegnati:
            frame_pt = ctk.CTkFrame(self.scrollable_frame)
            frame_pt.pack(fill="x", padx=10, pady=5)

            label_pt = ctk.CTkLabel(frame_pt, text=f"{pt['nome']}", font=ctk.CTkFont(size=14))
            label_pt.pack(side="left", padx=(0, 10))

            button_remove = ctk.CTkButton(frame_pt, text="-", command=lambda p=pt: self.rimuovi_pt(p))
            button_remove.pack(side="right")

    def rimuovi_pt(self, pt):
        if pt in self.pts_assegnati:
            self.pts_assegnati.remove(pt)
            messagebox.showinfo("Rimosso", f"PT {pt['nome']} rimosso dal corso")
        else:
            messagebox.showwarning("Attenzione", f"PT {pt['nome']} non è assegnato al corso")

    def conferma_modifiche(self):
        nome_nuovo = self.entry_nome.get()
        descrizione_nuova = self.entry_descrizione.get()

        # Esegue la callback per aggiornare le informazioni
        self.master.destroy()
        self.pts_assegnati_callback(self.id_corso, self.pts_assegnati, nome_nuovo, descrizione_nuova)
