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

                # Carica le variabili d'ambiente dal file .env
        load_dotenv()
        cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        print(f"Path to credentials: {cred_path}")


       

# Funzione per aggiungere l'orario alla raccolta "sistema"
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




