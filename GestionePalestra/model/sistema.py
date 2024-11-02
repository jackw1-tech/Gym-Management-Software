import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from tkinter import messagebox
db = firestore.client()
class Sistema:
    def __init__(self, cred_path, codice_gestore="KT9mvjyzAPRWqZBZGGbc"):
        load_dotenv()
        self.cred_path = cred_path or os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.codice_gestore = codice_gestore  # Codice gestore univoco
        self.sistema_ref = self.db.collection("sistema").document("unico_orario")  # Documento unico

               
        load_dotenv()
        cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        print(f"Path to credentials: {cred_path}")


    

    def aggiungi_orario(orario_settimanale):
        try:
            sistema_ref = db.collection(u'sistema').document(u'KT9mvjyzAPRWqZBZGGbc')  # ID fisso per un unico documento
        
            # Verifica se il documento esiste già
            if sistema_ref.get().exists:
                
                sistema_ref.update({
                u'orario_settimanale': orario_settimanale
                })
            else:
            # Prima esecuzione: crea il documento con campi predefiniti
                orario_data = {
                    u'orario_settimanale': orario_settimanale,
                    u'notifica': u'',  # Imposta notifica vuota
                    u'gestore': u'KT1ntbxlXMCTzUAXSSay'  # Imposta un codice per il gestore
                }
                sistema_ref.set(orario_data)  # Usa 'set' per creare il documento

            messagebox.showinfo("Successo", "Orario aggiornato correttamente!")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nell'aggiunta dell'orario: {e}")
    
    
    def get_orario_settimanale(self):
        """
        Restituisce solo l'orario settimanale dal documento.
        """
        dati = self.leggi_sistema()
        return dati.get("orario_settimanale") if dati else None
    
    def get_orario_settimanale_from_firebase(self):
        """
        Restituisce l'orario settimanale dal documento Firestore.
        """
        try:
            sistema_ref = db.collection('sistema').document('KT9mvjyzAPRWqZBZGGbc')
            doc = sistema_ref.get()
            
            if doc.exists:
                dati = doc.to_dict()
                orario_settimanale = dati.get('orario_settimanale', {})

                giorni_ordinati = ["Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
            
                orario_ordinato = {giorno: orario_settimanale.get(giorno, "") for giorno in giorni_ordinati}

                return orario_ordinato
               
            else:
                print("Il documento non esiste.")
                return None
        except Exception as e:
            print(f"Errore durante il recupero dell'orario settimanale: {e}")
            return None


    def ottieni_orari(orario_settimanale):
        giorni_settimana = [
            "Domenica",
            "Lunedì",
            "Martedì",
            "Mercoledì",
            "Giovedì",
            "Venerdì",
            "Sabato"
        ]

        orari_apertura = {}
        orari_chiusura = {}

        # Cicla attraverso i giorni e l'orario settimanale
        for giorno, orario in zip(giorni_settimana, orario_settimanale):
            apertura, chiusura = orario.split('-')  # Dividi la stringa in apertura e chiusura
            orari_apertura[giorno] = apertura
            orari_chiusura[giorno] = chiusura

        return orari_apertura, orari_chiusura




