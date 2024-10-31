import firebase_admin
from firebase_admin import credentials, firestore
from GestionePersonale.model.gestore import Gestore
db = firestore.client()
class pacchetto:
    def __init__(self, prezzo, nome, lista_corsi):
        self.prezzo = prezzo  
        self.listaCorsi = lista_corsi
        self.nome = nome

    def getPrezzo(self):
        return self.prezzo
    
    def aggiungi_pacchetto_a_firebase(self):
      
        pacchetto_data = {
            'nome': self.nome,
            'prezzo': self.prezzo,
            'lista_corsi': self.listaCorsi
        }
        
        try:
            doc_ref = db.collection('pacchetti').document()  
            doc_ref.set(pacchetto_data)
            Gestore.aggiungi_pacchetto_alla_lista(doc_ref.id)
        except Exception as e:
            print("Errore durante il caricamento del pacchetto su Firebase:", e)

    def recupera_dettagli_pacchetto(id_pacchetto):
        try:
           
            pacchetto_ref = db.collection("pacchetti").document(id_pacchetto)
            pacchetto = pacchetto_ref.get()
            if pacchetto.exists:
                return pacchetto.to_dict() 
            else:
                return None
        except Exception as e:
            print(f"Errore nel recupero del corso: {e}")
            return None
    def recupera_pacchetti_da_ids(lista_ids):
        pacchetti = [] 
        try:
            for id in lista_ids:
                doc_ref = db.collection('pacchetti').document(id)  
                doc = doc_ref.get() 
                
                if doc.exists: 
                    pacchetto_data = doc.to_dict()
                    pacchetto_data['id'] = id 
                    pacchetti.append(pacchetto_data)  
                else:
                    print(f"Documento con ID {id} non trovato.")
        except Exception as e:
            print("Errore durante il recupero dei pacchetti:", e)

        return pacchetti  

    def rimuovi_pacchetto_da_firebase(id_pachetto):
        from firebase_admin import firestore
        db = firestore.client()
        
        try:
            db.collection("pacchetti").document(id_pachetto).delete()
        except Exception as e:
            print(f"Errore durante l'eliminazione del pacchetto: {e}")
    
    def modifica_pacchetto(id_pacchetto, corsi_selezionati, nome_nuovo, prezzo_nuovo_float):
    
        try:
            pacchetto_ref = db.collection('pacchetti').document(id_pacchetto)
            pacchetto_doc = pacchetto_ref.get()

            if pacchetto_doc.exists:
                
                pacchetto_ref.update({
                    'lista_corsi':[corso['id'] for corso in corsi_selezionati],
                    'nome': nome_nuovo,
                    'prezzo' : prezzo_nuovo_float,
                })

                
            else:
                print(f"Pacchetto con ID {id_pacchetto} non trovato.")

        except Exception as e:
            print("Errore durante l'aggiornamento del pacchetto:", e)

    def rimuovi_corso_da_pacchetti(id_corso):
        try:
       
            pacchetti_ref = db.collection('pacchetti')
            pacchetti = pacchetti_ref.stream() 

            for pacchetto in pacchetti:
                pacchetto_data = pacchetto.to_dict()
                
             
                if 'lista_corsi' in pacchetto_data and id_corso in pacchetto_data['lista_corsi']:
               
                    nuova_lista_corsi = [corso for corso in pacchetto_data['lista_corsi'] if corso != id_corso]
                    
                    pacchetti_ref.document(pacchetto.id).update({
                        'lista_corsi': nuova_lista_corsi
                    })
                    

        except Exception as e:
            print("Errore durante la rimozione del corso dai pacchetti:", e)
