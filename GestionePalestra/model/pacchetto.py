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
        # Crea un dizionario con i dati del pacchetto
        pacchetto_data = {
            'nome': self.nome,
            'prezzo': self.prezzo,
            'lista_corsi': self.listaCorsi
        }
        
        try:
            doc_ref = db.collection('pacchetti').document()  
            doc_ref.set(pacchetto_data)
            Gestore.aggiungi_pacchetto_alla_lista(doc_ref.id)
            print(f"Pacchetto '{self.nome}' aggiunto con ID: {doc_ref.id}")
        except Exception as e:
            print("Errore durante il caricamento del pacchetto su Firebase:", e)

    
    def recupera_pacchetti_da_ids(lista_ids):
        pacchetti = []  # Lista per memorizzare i pacchetti recuperati
        try:
            for id in lista_ids:
                doc_ref = db.collection('pacchetti').document(id)  # Riferimento al documento con l'ID specificato
                doc = doc_ref.get()  # Recupera il documento
                
                if doc.exists:  # Verifica se il documento esiste
                    pacchetto_data = doc.to_dict()  # Ottieni i dati come dizionario
                    # Aggiungi il dizionario direttamente alla lista dei pacchetti
                    pacchetti.append(pacchetto_data)  
                else:
                    print(f"Documento con ID {id} non trovato.")
        except Exception as e:
            print("Errore durante il recupero dei pacchetti:", e)

        return pacchetti  # Restituisce la lista di pacchetti come dizionari

