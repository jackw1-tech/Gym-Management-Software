import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from GestionePalestra.model.corso import corso

# Carica le variabili d'ambiente dal file .env
load_dotenv()
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print(f"Path to credentials: {cred_path}")
# Ottieni il percorso della chiave dal file .env
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
print(f"Path to credentials: {cred_path}")
firebase_admin.initialize_app(cred)

# Stampa il percorso per il debug

db = firestore.client()

doc_ref = db.collection(u'membri').document(u'lorenzo_giannetti')
doc_ref.set({
    u'nome': u'Mario',
    u'cognome': u'Rosso',
    u'abbonamento': u'Gold',
    u'data_scadenza': u'2025-10-20'
})

c = corso("Thai","Doloroso")
doc_ref1 = db.collection(u'Corsi').document(c.getNome())
doc_ref1.set({
    u'nome':c.getNome() ,
    u'descrizione': c.getDescrizione(),
})

membri_ref = db.collection(u'membri')
membri_ref = db.collection(u'Corsi')
docs = membri_ref.get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))