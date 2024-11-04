
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from GestionePersonale.model.gestore import Gestore
import customtkinter as ctk
from firebase_admin import firestore


db = firestore.client()
class GestoreController:
    def __init__(self, view):
        self.view = view

    def crea_gestore(self, nome, cognome, username, password):
        try:
            gestore = Gestore(username= username, password= password, nome= nome, cognome= cognome)
            if gestore.crea_gestore_firebase():
                return True
            else:
                return False
            
        except Exception as e:
            print(f"Errore durante la creazione del gestore: {e}")
            return False

            
        