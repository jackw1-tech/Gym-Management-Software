import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv


load_dotenv()
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)
db = firestore.client()

class Gestore:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.lista_clienti = []
        self.lista_pt = []

    #def AggiungiAbbonamento(self, durata, prezzo, scadenza, listaclienti):
        #return Abbonamento(durata, prezzo, scadenza, listaclienti)

    #def aggiungiCorso(self, nome, descrizione):
        #return corso(nome, descrizione)


    #def AssegnaClientiPT(self, cliente, pt):
        # Logica per assegnare un cliente a un PT
        #pt.clienti.append(cliente)

    def AssegnaCorsoPacchetto(self, corso, pacchetto):
        # Aggiunge un corso a un pacchetto
        pacchetto.corsi.append(corso)

   # def AssegnaCorsoPT(self, corso, pt):
        # Assegna un corso a un PT
       # pt.corsi.append(corso)

    def AssegnaPacchettoAdAbbonamento(self, abbonamento, pacchetto):
        # Logica per assegnare un pacchetto a un abbonamento
        abbonamento.pacchetti.append(pacchetto)

    def getListaClienti(self):
        return self.lista_clienti

    def getListaPT(self):
        return self.lista_pt

    #def inserisciPT(self, nome, cognome, tariffa_oraria):
        pt = PT(nome, cognome, tariffa_oraria)
        self.lista_pt.append(pt)
        return pt
   
    def check_credentials_gestore(username, password):
        try:
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()
            if user.exists:
                user_data = user.to_dict()
                if user_data['username'] == username and user_data['password'] == password:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(f"Errore durante l'autenticazione: {e}")
            return False
