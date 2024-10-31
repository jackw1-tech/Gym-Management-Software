import customtkinter as ctk
from tkinter import messagebox

from GestionePalestra.controller.corso_controller import corso_controller

class CourseSearchView:
    def __init__(self, master, courses, home_callback):
        self.master = master
        self.master.title("Ricerca Corsi")
        self.master.geometry("700x600")
        self.home_callback = home_callback
        self.corso_controller = corso_controller(self)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.courses = courses
        self.filtered_courses = courses

        self.label_title = ctk.CTkLabel(master, text="Ricerca Corsi", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        self.search_entry = ctk.CTkEntry(master, placeholder_text="Cerca per nome corso", width=300)
        self.search_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(master, text="Cerca", command=self.search_courses)
        self.search_button.pack(pady=10)

        self.add_course_button = ctk.CTkButton(master, text="+ Aggiungi Corso", command=self.add_course)
        self.add_course_button.pack(pady=10)

        self.back_button = ctk.CTkButton(master, text="Indietro", command=self.go_back)
        self.back_button.pack(pady=10)

        # Frame per i risultati con scrollbar
        self.result_frame = ctk.CTkFrame(master)
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.scrollable_result_frame = ctk.CTkScrollableFrame(self.result_frame, width=660, height=400)
        self.scrollable_result_frame.pack(fill="both", expand=True)

        self.display_courses(self.filtered_courses[:5])
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
        self.home_callback(self) 
        
    def search_courses(self):
        query = self.search_entry.get().lower()
        self.filtered_courses = [course for course in self.courses if query in course['nome'].lower()]

        for widget in self.scrollable_result_frame.winfo_children():
            widget.destroy()

        self.display_courses(self.filtered_courses)

    def display_courses(self, courses_to_display):
        for index, course in enumerate(courses_to_display):
            # Nome corso allineato a sinistra
            name_label = ctk.CTkLabel(self.scrollable_result_frame, text=course['nome'], font=ctk.CTkFont(size=16))
            name_label.grid(row=index, column=0, padx=(10, 20), pady=10, sticky="w")  # Padding a destra per distanziare i pulsanti

            # Pulsanti allineati a destra, posizionati nelle ultime colonne
            button_view_details = ctk.CTkButton(self.scrollable_result_frame, text="Visualizza Dettagli", command=lambda c=course: self.view_details(c))
            button_view_details.grid(row=index, column=1, padx=5, pady=10, sticky="e")

            button_modify_course = ctk.CTkButton(self.scrollable_result_frame, text="Modifica Corso", command=lambda c=course: self.modify_course(c))
            button_modify_course.grid(row=index, column=2, padx=5, pady=10, sticky="e")

            button_delete_course = ctk.CTkButton(self.scrollable_result_frame, text="Elimina Corso", command=lambda c=course: self.delete_course(c))
            button_delete_course.grid(row=index, column=3, padx=5, pady=10, sticky="e")

        # Configura la colonna 0 per l’allineamento del nome del corso e le altre per l'allineamento dei tasti a destra
        self.scrollable_result_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_result_frame.grid_columnconfigure(1, weight=0)
        self.scrollable_result_frame.grid_columnconfigure(2, weight=0)
        self.scrollable_result_frame.grid_columnconfigure(3, weight=0)

    def aggiungi_corso_callback(self):
        self.corso_controller.open_course_search()
        
    def add_course(self):
        from GestionePalestra.controller.corso_controller import corso_controller
        self.master.destroy()
        c = corso_controller(self)
        c.crea_corso_view()
       

    def view_details(self, course):
        self.corso_controller.dettagli_corso_view(course['id'])
      

    def modify_course(self, course):
        self.master.destroy()
        self.corso_controller.modifica_corso_view(course['id'])
       

    def delete_course(self, course):
        messagebox.showinfo("Eliminato", f"Corso {course['nome']} eliminato")
        self.master.destroy()
        self.corso_controller.elimina_corso_view(course['id'], self.home_callback)
        