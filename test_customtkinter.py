import customtkinter

# Imposta il tema globale di CustomTkinter (opzionale)
customtkinter.set_appearance_mode("System")   # "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# Crea la finestra principale
root = customtkinter.CTk()
root.title("Test CustomTkinter")
root.geometry("400x300")

# Aggiungi un semplice pulsante CustomTkinter
button = customtkinter.CTkButton(
    master=root,
    text="Cliccami!",
    corner_radius=10,
    command=lambda: print("Pulsante premuto!")
)
button.pack(pady=40)

# Avvia il loop grafico
root.mainloop()

