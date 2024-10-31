import firebase_admin
from firebase_admin import credentials, firestore
from GestionePersonale.model.gestore import Gestore

db = firestore.client()
class corso:
    def __init__(self, nome, descrizione):
        self.nome = nome  
        self.descrizione = descrizione
        self.pt_assegnato = []  

    def getNome(self):
        return self.nome

    def getDescrizione(self):
        return self.descrizione

    def getPTAssegnato(self):
        return self.pt_assegnato

    def setNome(self, nome):
        self.nome = nome

    def setDescrizione(self, descrizione):
        self.descrizione = descrizione

    def assegnaPT(self, pt):
        self.pt_assegnato = pt
    
    def carica_corso_su_firebase(self):
        corso_data = {
            'nome': self.nome,
            'descrizione': self.descrizione,
            'pt_assegnato': []
        }
        try:
            
            doc_ref = db.collection('corsi').document()  
            doc_ref.set(corso_data) 
            Gestore.aggiungi_corso_alla_lista(doc_ref.id)
        except Exception as e:
            print("Errore durante il caricamento su Firebase:", e)
    
    
    def recupera_corsi_da_firebase_escludendo_ids(ids):
        corsi = [] 
        try:
            
            docs = db.collection('corsi').get() 
           
            for doc in docs:
                corso_data = doc.to_dict()
                corso_data['id'] = doc.id
                if corso_data['id'] not in ids:
                   
                    corsi.append(corso_data)  

        except Exception as e:
            print("Errore durante il recupero dei corsi da Firebase:", e)

        return corsi
    def recupera_corsi_da_firebase(ids):
        corsi = [] 
        try:
            for id in ids:
                doc_ref = db.collection('corsi').document(id)  
                doc = doc_ref.get()  
                
                if doc.exists:  
                    
                    corso_data = doc.to_dict()
                    corso_data['id'] = doc.id
                    corsi.append(corso_data)  
                else:
                    print(f"Documento con ID {id} non trovato.")
        except Exception as e:
            print("Errore durante il recupero dei corsi da Firebase:", e)

        return corsi  
    
    def get_document_id(stringa_corso):
        nome = stringa_corso['nome']
        pt_assegnato = stringa_corso['pt_assegnato']
        descrizione = stringa_corso['descrizione']
        try:
           
            corsi_ref = db.collection('corsi')  
            query = corsi_ref.where('nome', '==', nome).where('pt_assegnato', '==', pt_assegnato).where('descrizione', '==', descrizione)
            results = query.get()

           
            if results:
                for doc in results:
                    return doc.id
            else:
                print("Nessun documento trovato con i criteri specificati.")
                return None
        except Exception as e:
            print("Errore durante la ricerca del documento:", e)
            return None
        
    def aggiorna_pt_al_corso(pt_id, corso_id, tipo):
        
        pt_id = pt_id.replace("'", "").strip()
        pt_id = pt_id.replace("{", "").strip()
        pt_id = pt_id.replace("}", "").strip()
        

        corso_ref = db.collection('corsi').document(str(corso_id))
        corso = corso_ref.get()
        
        if corso.exists:
          
            pt_esistente = corso.to_dict().get("pt_assegnato", [])
            
            if tipo == "+":
                
                if pt_id not in pt_esistente:
                    pt_esistente.append(pt_id)
            elif tipo == "-":
                
                if pt_id in pt_esistente:
                    pt_esistente.remove(pt_id)
            
           
            corso_ref.update({"pt_assegnato": pt_esistente})

            
    def rimuovi_corso_da_firebase(id):
       
        from firebase_admin import firestore
        db = firestore.client()
        
        try:
            db.collection("corsi").document(id).delete()
        except Exception as e:
            print(f"Errore durante l'eliminazione del corso: {e}")
    
    def recupera_dettagli_corso(id_corso):
        try:
            
            corso_ref = db.collection("corsi").document(id_corso)
            corso = corso_ref.get()
            if corso.exists:
                return corso.to_dict()
            else:
                return None
        except Exception as e:
            print(f"Errore nel recupero del corso: {e}")
            return None
    
    def modifica_corso(id_corso, pt_selezionati, nome_nuovo, nuova_descrizione):
        try:
            
            corso_ref = db.collection('corsi').document(id_corso)
            corso_doc = corso_ref.get()

            if corso_doc.exists:
                
                corso_ref.update({
                    'pt_assegnato':[pt['id'] for pt in pt_selezionati],
                    'nome': nome_nuovo,
                    'descrizione' : nuova_descrizione,
                })

                
            else:
                print(f"corso non trovato.")

        except Exception as e:
            print("Errore durante l'aggiornamento del corso:", e)