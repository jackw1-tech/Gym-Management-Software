import customtkinter as ctk
from login.view.login import LoginScreen  

if __name__ == "__main__":
    root = ctk.CTk()  
    login_screen = LoginScreen(root)
    root.mainloop()