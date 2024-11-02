import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.view.aggiungi_pacchetti_view import AggiungiPacchettoView
from GestionePalestra.controller.pacchetto_controller import pacchetto_controller

class CoursePackageSearchView:
    def __init__(self, master, packages, home_callback):
        self.master = master
        self.master.title("Ricerca Pacchetti di Corsi")
        self.master.geometry("700x600")
        self.home_callback = home_callback
        self.pacchetto_controller = pacchetto_controller(self)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.packages = packages
        self.filtered_packages = packages

        self.label_title = ctk.CTkLabel(master, text="Ricerca Pacchetti di Corsi", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        self.search_entry = ctk.CTkEntry(master, placeholder_text="Cerca per nome pacchetto", width=300)
        self.search_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(master, text="Cerca", command=self.search_packages)
        self.search_button.pack(pady=10)

        self.add_package_button = ctk.CTkButton(master, text="+ Aggiungi Pacchetto", command=self.add_package)
        self.add_package_button.pack(pady=10)

        self.back_button = ctk.CTkButton(master, text="Indietro", command=self.go_back)
        self.back_button.pack(pady=10)
        
        
        self.result_frame = ctk.CTkFrame(master)
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.scrollable_result_frame = ctk.CTkScrollableFrame(self.result_frame, width=660, height=400)
        self.scrollable_result_frame.pack(fill="both", expand=True)
        
        self.display_packages(self.filtered_packages[:5])
        self.center_window()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 700
        window_height = 600
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def go_back(self):
        self.master.destroy()
        self.home_callback() 
        
    def search_packages(self):
        query = self.search_entry.get().lower()
        self.filtered_packages = [package for package in self.packages if query in package['nome'].lower()]

        for widget in self.scrollable_result_frame.winfo_children():
            widget.destroy()

        self.display_packages(self.filtered_packages)

    def display_packages(self, packages_to_display):
        for index, package in enumerate(packages_to_display):
      
            name_label = ctk.CTkLabel(self.scrollable_result_frame, text=package['nome'], font=ctk.CTkFont(size=16))
            name_label.grid(row=index, column=0, padx=(10, 20), pady=10, sticky="w")  

        
            button_view_details = ctk.CTkButton(self.scrollable_result_frame, text="Visualizza Dettagli", command=lambda p=package: self.view_details(p))
            button_view_details.grid(row=index, column=1, padx=5, pady=10, sticky="e")

            button_modify_package = ctk.CTkButton(self.scrollable_result_frame, text="Modifica Pacchetto", command=lambda p=package: self.modify_package(p))
            button_modify_package.grid(row=index, column=2, padx=5, pady=10, sticky="e")

            button_delete_package = ctk.CTkButton(self.scrollable_result_frame, text="Elimina Pacchetto", command=lambda p=package: self.delete_package(p))
            button_delete_package.grid(row=index, column=3, padx=5, pady=10, sticky="e")


        self.scrollable_result_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_result_frame.grid_columnconfigure(1, weight=0)
        self.scrollable_result_frame.grid_columnconfigure(2, weight=0)
        self.scrollable_result_frame.grid_columnconfigure(3, weight=0)

    def aggiugni_pacchetto_callback(self):
        self.pacchetto_controller.open_course_package_search()
        
    def add_package(self):
        self.master.destroy()
        root  = ctk.CTk()
        AggiungiPacchettoView(root, self.aggiugni_pacchetto_callback, [], self.home_callback)
        root.mainloop()

    def view_details(self, package):
        self.pacchetto_controller.dettagli_pacchetto_view(package['id'])
      

    def modify_package(self, package):
        self.master.destroy()
        self.pacchetto_controller.modifica_pacchetto_view(package['id'])
       

    def delete_package(self, package):
        messagebox.showinfo("Eliminato", f"Pacchetto {package['nome']} eliminato")
        self.master.destroy()
        self.pacchetto_controller.elimina_pacchetto_view(package['id'], self.home_callback)
