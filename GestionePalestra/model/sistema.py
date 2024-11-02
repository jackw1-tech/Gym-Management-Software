import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from tkinter import messagebox

db = firestore.client()
class Sistema:
    def __init__(self, gestore):
        self.gestore = gestore  
        self.orario_settimanale = []
        self.notifica = []

    def aggiungi_orario(orario_settimanale):
        try:
            sistema_ref = db.collection(u'sistema').document(u'KT9mvjyzAPRWqZBZGGbc')
            if sistema_ref.get().exists:
                sistema_ref.update({
                u'orario_settimanale': orario_settimanale
                })
            else:
        
                orario_data = {
                    u'orario_settimanale': orario_settimanale,
                    u'notifica': u'',  
                    u'gestore': u'KT1ntbxlXMCTzUAXSSay' 
                }
                sistema_ref.set(orario_data) 

            messagebox.showinfo("Successo", "Orario aggiornato correttamente!")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nell'aggiunta dell'orario: {e}")
    
    def get_orario_settimanale(self):
        dati = self.sistema_ref.get().to_dict()
        return dati.get("orario_settimanale") if dati else None
    
    def get_orari_esistenti():
        try:
            sistema_ref = db.collection("sistema").document("KT9mvjyzAPRWqZBZGGbc")
            doc = sistema_ref.get()
            if doc.exists:
                return doc.to_dict().get("orario_settimanale", {})
            return {}
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel recupero dell'orario: {e}")
            return {}

