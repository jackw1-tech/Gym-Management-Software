import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
from GestionePersonale.model.gestore import Gestore



db = firestore.client()
class PT:
    def __init__(self, nome, cognome, stipendio, username, password):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
        self.username = username
        self.password = password
        self.clienti = []
        self.corsi = []

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getStipendio(self):
        return self.stipendio

    def getListaClienti(self):
        return self.clienti

    def getListaCorsi(self):
        return self.corsi

    def inserisciNome(self, nome):
        self.nome = nome

    def inserisciCognome(self, cognome):
        self.cognome = cognome

    def inserisciStipendio(self, stipendio):
        self.stipendio = stipendio
    
    def check_credentials_gestore(username, password):
        try:
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()
            if user.exists:
                user_data = user.to_dict()
                for pt_id in user_data['pt']:
                    pt_ref = db.collection('pt').document(pt_id)
                    pt = pt_ref.get()
                    pt_data = pt.to_dict()
                    if pt_data['username'] == username and pt_data['password'] == password:
                        return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(f"Errore durante l'autenticazione: {e}")
            return False
        
    def salva_su_firebase(self):
        pt_data = {
            'nome': self.nome,
            'cognome': self.cognome,
            'stipendio': self.stipendio,
            'username': self.username,
            'password': self.password,
            'clienti': [],
            'corsi': []
        }

        try:
            # Inserire il documento nella collezione "pt"
            pt_ref = db.collection('pt').add(pt_data)  # Questo crea automaticamente un nuovo documento con ID univoco
            print(f"Documento creato con ID: {pt_ref[1].id}")
            Gestore.aggiungi_pt_alla_lista(pt_ref[1].id)
        except Exception as e:
            print(f"Errore durante l'inserimento su Firebase: {e}")

   