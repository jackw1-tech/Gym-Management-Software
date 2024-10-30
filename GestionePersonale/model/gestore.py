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
        self.lista_corsi = []

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
        from GestionePersonale.model.pt import PT
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
                            p = PT.manda_in_ferie(pt_data['id'])
                            lista_pt.append(p)
                          
                            
                            
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
    

    def aggiungi_corso_alla_lista(id_corso):
        try:
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()
            if user.exists:
                user_data = user.to_dict()
                
                if 'corsi' in user_data:
                    corsi_list = user_data['corsi']
                    if id_corso not in corsi_list:
                        corsi_list.append(id_corso)
                        user_ref.update({'corsi': corsi_list})  # Aggiorna il documento con la nuova lista
                else:
                    # Se il campo 'pt' non esiste, lo crea con il nuovo ID
                    user_ref.update({'corsi': [id_corso]})
                    print(f"Lista 'pt' creata e ID {id_corso} aggiunto correttamente.")
                
            else:
                print("Documento del gestore non trovato.")
                return False
        except Exception as e:
            print(f"Errore durante l'aggiornamento della lista 'pt': {e}")
            return False
    
    def aggiungi_pacchetto_alla_lista(id_pacchetto):
        try:
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()
            if user.exists:
                user_data = user.to_dict()
                
                if 'pacchetti' in user_data:
                    pacchetti_list = user_data['pacchetti']
                    if id_pacchetto not in pacchetti_list:
                        pacchetti_list.append(id_pacchetto)
                        user_ref.update({'pacchetti': pacchetti_list})  # Aggiorna il documento con la nuova lista
                else:
                    # Se il campo 'pt' non esiste, lo crea con il nuovo ID
                    user_ref.update({'pacchetti': [id_pacchetto]})
                    print(f"Lista 'pt' creata e ID {id_pacchetto} aggiunto correttamente.")
                
            else:
                print("Documento del gestore non trovato.")
                return False
        except Exception as e:
            print(f"Errore durante l'aggiornamento della lista 'pt': {e}")
            return False
    
    def recupera_corsi_dal_documento_gestore():
        try:
            # Ottieni il riferimento al documento del gestore
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()

            # Verifica se il documento esiste
            if user.exists:
                user_data = user.to_dict()
                # Controlla se esiste la chiave 'corsi'
                if 'corsi' in user_data:
                    return user_data['corsi']  # Restituisce la lista di corsi
                else:
                    print("La sezione 'corsi' non è presente nel documento.")
                    return []
            else:
                print("Documento del gestore non trovato.")
                return []
        except Exception as e:
            print(f"Errore durante il recupero della lista 'corsi': {e}")
            return []
        
    def recupera_pacchetti_dal_documento_gestore():
        try:
            # Ottieni il riferimento al documento del gestore
            user_ref = db.collection('gestore').document("KT1ntbxlXMCTzUAXSSay")
            user = user_ref.get()

            # Verifica se il documento esiste
            if user.exists:
                user_data = user.to_dict()
                
                if 'pacchetti' in user_data:
                    return user_data['pacchetti']  # Restituisce la lista di corsi
                else:
                    print("La sezione 'pacchetti' non è presente nel documento.")
                    return []
            else:
                print("Documento del gestore non trovato.")
                return []
        except Exception as e:
            print(f"Errore durante il recupero della lista 'corsi': {e}")
            return []