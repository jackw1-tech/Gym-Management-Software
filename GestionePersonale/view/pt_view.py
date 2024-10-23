import tkinter as tk
from tkinter import messagebox

class PTView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Management Software - Personal Trainer Menu")
        self.master.geometry("300x200")

        # Messaggio di benvenuto
        self.welcome_label = tk.Label(master, text="Benvenuto nella sezione Personal Trainer!")
        self.welcome_label.pack(pady=10)

        # Pulsanti per le diverse funzionalità
        self.courses_button = tk.Button(master, text="Corsi", command=self.manage_courses)
        self.courses_button.pack(pady=5)

        self.other_button = tk.Button(master, text="Altro", command=self.manage_other)
        self.other_button.pack(pady=5)

        self.clients_button = tk.Button(master, text="Clienti", command=self.manage_clients)
        self.clients_button.pack(pady=5)

    def manage_courses(self):
        messagebox.showinfo("Corsi", "Apertura della sezione Corsi.")

    def manage_other(self):
        messagebox.showinfo("Altro", "Apertura della sezione Altro.")

    def manage_clients(self):
        messagebox.showinfo("Clienti", "Apertura della sezione Clienti.")

# Esempio di utilizzo
if __name__ == "__main__":
    root = tk.Tk()
    pt_view = PTView(root)
    root.mainloop()