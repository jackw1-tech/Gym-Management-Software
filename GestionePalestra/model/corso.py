import firebase_admin
from firebase_admin import credentials, firestore
from GestionePersonale.model.gestore import Gestore

db = firestore.client()
class corso:
    def __init__(self, nome, descrizione):
        self.nome = nome  # Nome del corso
        self.descrizione = descrizione  # Descrizione del corso
        self.pt_assegnato = None  # PT (Personal Trainer) assegnato al corso

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
            'pt_assegnato': self.pt_assegnato if self.pt_assegnato else None
        }
        try:
            
            doc_ref = db.collection('corsi').document()  # Crea un documento vuoto con ID generato
            doc_ref.set(corso_data)  # Aggiunge i dati al document
            Gestore.aggiungi_corso_alla_lista(doc_ref.id)
        except Exception as e:
            print("Errore durante il caricamento su Firebase:", e)
            
            
    def recupera_corsi_da_firebase(ids):
        corsi = []  # Lista per memorizzare i corsi recuperati
        try:
            for id in ids:
                print("ciao" + str(id))
                doc_ref = db.collection('corsi').document(id)  # Riferimento al documento con l'ID specificato
                doc = doc_ref.get()  
                print(doc.to_dict())
                if doc.exists:  # Verifica se il documento esiste
                    # Trasforma i dati in una tupla
                    corso_data = doc.to_dict()
                    corsi.append(corso_data)  # Aggiungi la tupla alla lista dei corsi
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
            # Crea una query per cercare il documento con i valori specificati
            corsi_ref = db.collection('corsi')  # Sostituisci 'corsi' con il nome della tua collezione
            query = corsi_ref.where('nome', '==', nome).where('pt_assegnato', '==', pt_assegnato).where('descrizione', '==', descrizione)
            results = query.get()

            # Controlla se ci sono risultati e restituisci gli ID dei documenti trovati
            if results:
                for doc in results:
                    print(f"Documento trovato con ID: {doc.id}")
                    return doc.id  # Restituisce il primo ID trovato
            else:
                print("Nessun documento trovato con i criteri specificati.")
                return None
        except Exception as e:
            print("Errore durante la ricerca del documento:", e)
            return None