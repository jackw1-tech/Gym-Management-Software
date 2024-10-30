from datetime import datetime
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
        self.stato = "disponibile"
        self.data_inizio_ferie = None
        self.data_fine_ferie = None

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
            'corsi': [],
            'stato': 'disponibile',
            'data_inizio': "",
            'data_fine' : "",
        }
        

        try:
            # Inserire il documento nella collezione "pt"
            pt_ref = db.collection('pt').add(pt_data)  # Questo crea automaticamente un nuovo documento con ID univoco
            
            Gestore.aggiungi_pt_alla_lista(pt_ref[1].id)
        except Exception as e:
            print(f"Errore durante l'inserimento su Firebase: {e}")
    
    def cambia_stato_pt(self,id_document,stato):
        pt_ref = db.collection('pt').document(id_document)

        pt = pt_ref.get()
        if pt.exists:
            pt_ref.update({"stato": stato})
    
    def manda_in_ferie(id_document):
        pt_ref = db.collection('pt').document(id_document)
        pt = pt_ref.get()
        
        if pt.exists:
            stato = pt.get("stato")
            if stato != 'Inattivo':
                data_inizio = pt.get("data_inizio")
                data_fine = pt.get("data_fine")
                

                if data_inizio and data_fine: 
                    data_inizio = datetime.strptime(data_inizio, "%d/%m/%Y")
                    data_fine = datetime.strptime(data_fine, "%d/%m/%Y")
                    oggi = datetime.now()

                    if data_inizio <= oggi <= data_fine:
                        pt_ref.update({"stato": "In ferie"})
                    elif oggi > data_fine or oggi < data_inizio:
                        pt_ref.update({"stato": "Disponibile"})
                        
                
                # Reset delle date e stato
                else:
                    pt_ref.update({
                        "data_inizio": "",
                        "data_fine": "",
                        "stato": "Disponibile"
                    })
        pt_ref = db.collection('pt').document(id_document)
        pt = pt_ref.get()
        pt_data = pt.to_dict()
        pt_data['id'] = id_document
        return pt_data
            
    def ottieni_corsi_attuali_pt(id_document):
        from GestionePersonale.model.pt import PT
        lista_corsi = []
        id_document = id_document.replace("'", "").strip()
        id_document = id_document.replace("{", "").strip()
        id_document = id_document.replace("}", "").strip()
        try:
            user_ref = db.collection('pt').document(id_document)
            user = user_ref.get()
            if user.exists:
                user_data = user.to_dict()
                if 'corsi' in user_data:
                    corsi = user_data['corsi']
                    
                    # Controlla se corsi è un set e converti in lista
                    if isinstance(corsi, set):
                        corsi = list(corsi)
                    elif not isinstance(corsi, list):
                        return []

                    for documento in corsi:
                        corsi_ref = db.collection('corsi').document(documento)
                        corso = corsi_ref.get()
                        if corso.exists:  # Verifica che il documento esista
                            corso_data = corso.to_dict()
                            corso_data['id'] = corso.id  # Aggiungi l'ID del corso
                            lista_corsi.append(corso_data)
                        
                            
                    return lista_corsi
                else:
                
                    return []
            else:
                return []
        except Exception as e:
            print(f"Errore durante il recupero della lista 'corsi': {e}")
            return []

             
    def ottieni_corsi_non_attuali_pt(id_document):
        lista_corsi_attuali = PT.ottieni_corsi_attuali_pt(id_document)
        lista_corsi_attuali_ids = {corso['id'] for corso in lista_corsi_attuali}  # Supponendo che ogni corso abbia un campo 'id'

        lista_corsi_non_attuali = []
        try:
            corsi_ref = db.collection('corsi').stream()
            for corso in corsi_ref:
                corso_data = corso.to_dict()
                corso_data['id'] = corso.id
             
                if corso_data['id'] not in lista_corsi_attuali_ids:
                    lista_corsi_non_attuali.append(corso_data)
            
            return lista_corsi_non_attuali
        except Exception as e:
            print(f"Errore durante il recupero dei corsi non attuali: {e}")
            return []
    
        
    def aggiorna_dati(self, id_document,nome,cognome,stipendio,username,password,stato,data_inizio,data_fine):
       
        pt_ref = db.collection('pt').document(id_document)

        pt = pt_ref.get()
        if pt.exists:
            pt_ref.update({"nome": nome})
            pt_ref.update({"cognome": cognome})
            pt_ref.update({"stipendio": stipendio})
            pt_ref.update({"username": username})
            pt_ref.update({"password": password})
            if(stato == 'In ferie'):
                pt_ref.update({"data_inizio": data_inizio})
                pt_ref.update({"data_fine": data_fine})
            else:
                pt_ref.update({"data_inizio": ""})
                pt_ref.update({"data_fine": ""})
            
            if(stato == 'Inattivo'):
                pt_ref.update({"stato": "Inattivo"})
            else:
                PT.manda_in_ferie(id_document)
    
   
    def aggiorna_corsi_pt(pt_id,corso_id,tipo):
        pt_id = pt_id.replace("'", "").strip()
        pt_id = pt_id.replace("{", "").strip()
        pt_id = pt_id.replace("}", "").strip()
        pt_ref = db.collection('pt').document(str(pt_id))
        pt = pt_ref.get()
        if pt.exists:
            corsi_esistenti = pt.to_dict().get("corsi", [])
            if tipo == "+":
                corsi_esistenti.append(corso_id)
            elif tipo == "-":
                if corso_id in corsi_esistenti:
                 corsi_esistenti.remove(corso_id)
            pt_ref.update({"corsi": corsi_esistenti})