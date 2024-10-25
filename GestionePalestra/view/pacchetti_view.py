import customtkinter as ctk
from tkinter import messagebox
from GestionePalestra.view.aggiungi_pacchetti_view import AggiungiPacchettoView

class CoursePackageSearchView:
    def __init__(self, master, packages):
        self.master = master
        self.master.title("Ricerca Pacchetti di Corsi")
        self.master.geometry("700x500")
        
        # Imposta il tema e i colori
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Lista dei pacchetti di corsi
        self.packages = packages
        self.filtered_packages = packages  # Lista filtrata

        # Label del titolo
        self.label_title = ctk.CTkLabel(master, text="Ricerca Pacchetti di Corsi", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # Campo di ricerca
        self.search_entry = ctk.CTkEntry(master, placeholder_text="Cerca per nome pacchetto", width=300)
        self.search_entry.pack(pady=10)

        # Pulsante di ricerca
        self.search_button = ctk.CTkButton(master, text="Cerca", command=self.search_packages)
        self.search_button.pack(pady=10)

        # Pulsante per aggiungere nuovo pacchetto di corsi
        self.add_package_button = ctk.CTkButton(master, text="+ Aggiungi Pacchetto", command=self.add_package)
        self.add_package_button.pack(pady=10)

        # Frame per visualizzare i risultati
        self.result_frame = ctk.CTkFrame(master)
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Visualizza i primi 5 pacchetti di corsi
        self.display_packages(self.filtered_packages[:5])

    def search_packages(self):
        query = self.search_entry.get().lower()
        self.filtered_packages = [package for package in self.packages if query in package['nome'].lower()]

        # Cancella il contenuto precedente e visualizza i risultati filtrati
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        self.display_packages(self.filtered_packages[:5])

    def display_packages(self, packages_to_display):
        for index, package in enumerate(packages_to_display):
            # Nome pacchetto a sinistra
            name_label = ctk.CTkLabel(self.result_frame, text=package['nome'], font=ctk.CTkFont(size=16))
            name_label.grid(row=index, column=0, padx=10, pady=10, sticky="w")

            # Pulsanti allineati a destra sulla stessa riga
            button_view_details = ctk.CTkButton(self.result_frame, text="Visualizza Dettagli", command=lambda p=package: self.view_details(p))
            button_view_details.grid(row=index, column=1, padx=5, pady=10, sticky="e")

            button_modify_package = ctk.CTkButton(self.result_frame, text="Modifica Pacchetto", command=lambda p=package: self.modify_package(p))
            button_modify_package.grid(row=index, column=2, padx=5, pady=10, sticky="e")

            button_delete_package = ctk.CTkButton(self.result_frame, text="Elimina Pacchetto", command=lambda p=package: self.delete_package(p))
            button_delete_package.grid(row=index, column=3, padx=5, pady=10, sticky="e")

    def aggiugni_pacchetto_callback():
        print("ciao")
    def add_package(self):
        root = ctk.CTkToplevel()
        AggiungiPacchettoView(root, self.aggiugni_pacchetto_callback)
        root.mainloop()

    def view_details(self, package):
        print(f"Visualizza dettagli per {package['nome']}")

    def modify_package(self, package):
        print(f"Modifica pacchetto {package['nome']}")

    def delete_package(self, package):
        print(f"Elimina pacchetto {package['nome']}")
        # Simula l'eliminazione del pacchetto
        # Per esempio, modifica lo stato nel database
        # Mostra un popup di conferma
        messagebox.showinfo("Eliminato", f"Pacchetto {package['nome']} eliminato")
        
        # Ricarica la vista dei risultati
        self.search_packages()