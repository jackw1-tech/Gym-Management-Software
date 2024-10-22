# main.py

import tkinter as tk
from login.view.login import LoginScreen  # Importa la classe LoginScreen dal file login_screen.py

if __name__ == "__main__":
    root = tk.Tk()  # Crea la finestra principale di Tkinter
    login_screen = LoginScreen(root)  # Crea un'istanza della classe LoginScreen
    root.mainloop()  # Avvia il loop principale di Tkinter