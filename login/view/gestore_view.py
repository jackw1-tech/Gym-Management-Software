# view.py
import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Management Software - Main Menu")
        self.master.geometry("300x200")

        # Messaggio di benvenuto
        self.welcome_label = tk.Label(master, text="Welcome to the Gym Management System!")
        self.welcome_label.pack(pady=10)

        # Pulsanti per le diverse funzionalità
        self.management_button = tk.Button(master, text="Gestione Palestra", command=self.manage_gym)
        self.management_button.pack(pady=5)

        self.staff_button = tk.Button(master, text="Personale", command=self.manage_staff)
        self.staff_button.pack(pady=5)

        self.accounting_button = tk.Button(master, text="Contabilità", command=self.manage_accounting)
        self.accounting_button.pack(pady=5)

        self.clients_button = tk.Button(master, text="Clienti", command=self.manage_clients)
        self.clients_button.pack(pady=5)

    def manage_gym(self):
        messagebox.showinfo("Gestione Palestra", "Apertura della sezione Gestione Palestra.")

    def manage_staff(self):
        messagebox.showinfo("Personale", "Apertura della sezione Personale.")

    def manage_accounting(self):
        messagebox.showinfo("Contabilità", "Apertura della sezione Contabilità.")

    def manage_clients(self):
        messagebox.showinfo("Clienti", "Apertura della sezione Clienti.")


