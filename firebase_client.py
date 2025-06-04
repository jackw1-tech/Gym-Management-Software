
import os
import firebase_admin
from firebase_admin import credentials, firestore

def get_firestore_client():
    """
    Inizializza (se non già inizializzato) l’Admin SDK di Firebase
    e restituisce il client Firestore da usare nel DAO.
    Il file delle credenziali viene preso da:
      - variabile d’ambiente GOOGLE_APPLICATION_CREDENTIALS
      - altrimenti da "credentials/firebase_service_account.json"
    """
    if not firebase_admin._apps:
        # Prova a leggere la variabile d’ambiente; altrimenti usa il path di default
        cred_path = os.getenv(
            "GOOGLE_APPLICATION_CREDENTIALS",
            "progetto-ing-del-software-firebase-adminsdk-ogjqx-f260a3978a.json"
        )
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

    # Restituisce il client Firestore per poter fare query, read/write, ecc.
    return firestore.client()
