import customtkinter as ctk
from login.view.login import LoginScreen  

if __name__ == "__main__":
    root = ctk.CTk()  # Usa CTk invece di Tk per mantenere gli aspetti grafici di CustomTkinter
    login_screen = LoginScreen(root)  # Crea la schermata di login
    root.mainloop()  # Avvia il ciclo principale dell'applicazione