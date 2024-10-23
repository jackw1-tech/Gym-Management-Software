import tkinter as tk
from login.view.login import LoginScreen  

if __name__ == "__main__":
    root = tk.Tk()  
    login_screen = LoginScreen(root)  
    root.mainloop()
    
    