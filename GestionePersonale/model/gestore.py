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

    def aggiungi_pt_alla_lista(id_pt):
        try:
            # Ottenere il riferimento al documento del gestore
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()

            # Verificare se il documento esiste
            if user.exists:
                user_data = user.to_dict()

                # Aggiungere l'ID passato come parametro all'array 'pt' solo se non è già presente
                if 'pt' in user_data:
                    pt_list = user_data['pt']

                    
                    if id_pt not in pt_list:
                        pt_list.append(id_pt)
                        user_ref.update({'pt': pt_list})  # Aggiorna il documento con la nuova lista
                        print(f"ID {id_pt} aggiunto correttamente alla lista 'pt'.")
                    else:
                        print(f"ID {id_pt} è già presente nella lista 'pt'.")
                else:
                    # Se il campo 'pt' non esiste, lo crea con il nuovo ID
                    user_ref.update({'pt': [id_pt]})
                    print(f"Lista 'pt' creata e ID {id_pt} aggiunto correttamente.")
                
            else:
                print("Documento del gestore non trovato.")
                return False
        except Exception as e:
            print(f"Errore durante l'aggiornamento della lista 'pt': {e}")
            return False
    def get_lista_pt(self):
        lista_pt = []
        try:
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()

            if user.exists:
                user_data = user.to_dict()
                if 'pt' in user_data:
                    for documento in user_data['pt']:
                        pt_ref = db.collection('pt').document(documento)
                        pt = pt_ref.get()
                        pt_data = pt.to_dict()
                        pt_data['id'] = pt.id
                        if(pt_data['stato'] != 'cancellato'):
                            lista_pt.append(pt_data)
                    print(lista_pt)
                    return lista_pt
                else:
                    return []
            else:
                print("Documento del gestore non trovato.")
                return []
        except Exception as e:
            print(f"Errore durante il recupero della lista 'pt': {e}")
            return []
        