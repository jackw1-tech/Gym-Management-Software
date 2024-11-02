import customtkinter as ctk
from tkinter import messagebox
from GestionePersonale.controller.pt_controller import PTController
from GestionePersonale.model.pt import PT
from GestionePalestra.view.modifica_pt_view import ModificaPTView

class PersonalTrainerSearchView:
    def __init__(self, master, trainers, back_function):
        self.master = master
        self.master.title("Ricerca Personal Trainer")
        self.master.geometry("700x600")
        self.controller = PTController(self)
        self.back = back_function
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        
        self.trainers = trainers
        self.filtered_trainers = trainers

        
        self.label_title = ctk.CTkLabel(master, text="Ricerca Personal Trainer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

       
        self.search_entry = ctk.CTkEntry(master, placeholder_text="Cerca per nome o cognome", width=300)
        self.search_entry.pack(pady=10)

       
        self.search_button = ctk.CTkButton(master, text="Cerca", command=self.search_trainers)
        self.search_button.pack(pady=10)

      
        self.back_button = ctk.CTkButton(master, text="Torna Indietro", command=self.torna_indietro)
        self.back_button.pack(pady=10)

      
        self.result_frame = ctk.CTkFrame(master)
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=10)

        
        self.display_trainers(self.filtered_trainers[:8])
        self.center_window()

    def center_window(self):
       
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()


        window_width = 700
        window_height = 600

 
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

       
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")


    def search_trainers(self):
        query = self.search_entry.get().lower()
        self.filtered_trainers = [trainer for trainer in self.trainers if query in trainer['nome'].lower() or query in trainer['cognome'].lower()]
        
        
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        self.display_trainers(self.filtered_trainers[:5])

    def display_trainers(self, trainers_to_display):
        for index, trainer in enumerate(trainers_to_display):
     
            name_label = ctk.CTkLabel(self.result_frame, text=f"{trainer['nome']} {trainer['cognome']}", font=ctk.CTkFont(size=16))
            name_label.grid(row=index, column=0, padx=10, pady=10, sticky="w")

            if(trainer['stato'] == 'Disponibile'):
                button_assign_courses = ctk.CTkButton(self.result_frame, text="Assegna Corsi", command=lambda t=trainer: self.assign_courses(t))
                button_assign_courses.grid(row=index, column=1, padx=5, pady=10, sticky="e")

            button_modify_pt = ctk.CTkButton(self.result_frame, text="Modifica PT", command=lambda t=trainer: self.modify_pt(t))
            button_modify_pt.grid(row=index, column=2, padx=5, pady=10, sticky="e")

            button_delete_pt = ctk.CTkButton(self.result_frame, text="Elimina PT", command=lambda t=trainer: self.delete_pt(t))
            button_delete_pt.grid(row=index, column=3, padx=5, pady=10, sticky="e")

    def assign_courses(self, trainer):
        self.master.destroy() 
        self.controller.assegna_corsi_view(str({trainer['id']}))

    def modify_pt(self, trainer):
        self.master.destroy() 
        root = ctk.CTk()  
        ModificaPTView(root, self.controller.get_view_trova_pt, trainer) 
        root.mainloop()

    def torna_indietro(self):
        self.master.destroy() 
        self.back()

    def delete_pt(self, trainer):
        
        print(f"Elimina {trainer['nome']} {trainer['cognome']}")
        print(trainer['id'])
        PT.cambia_stato_pt(self, trainer['id'], "cancellato")
  
        messagebox.showinfo("Eliminato", f"PT {trainer['nome']} {trainer['cognome']} eliminato")
        self.master.destroy()
        self.back()
        
