from firebase_client import get_firestore_client
from GestioneClienti.dao.base_dao import BaseDAO
from GestioneClienti.model.Cliente import Cliente
from typing import List, Optional

class ClienteDaoFirebase(BaseDAO):
    def __init__(self):
        self.db = get_firestore_client()
        self.collection = self.db.collection("clienti")

    def fetch_all(self) -> List[Cliente]:
        docs = self.collection.stream()
        return [Cliente.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def create_cliente(self, cliente: Cliente) -> str:
        cliente_dict = cliente.to_dict()
        doc_ref = self.collection.add(cliente_dict)
        return doc_ref[1].id

    def delete(self, id):
        raise NotImplementedError("delete non implementato")

    def fetch_by_id(self, id):
        raise NotImplementedError("fetch_by_id non implementato")

    def update(self, id, dati):
        raise NotImplementedError("update non implementato")
    
    # Abbonamenti
    def fetch_abbonamenti_by_cliente_id(self, cliente_id: str) -> List[dict]:
        """
        Recupera tutti gli abbonamenti associati a un cliente specifico.
        """
        abbonamenti_ref = self.db.collection("abbonamenti")
        query = abbonamenti_ref.where("id_cliente", "==", cliente_id)
        docs = query.stream()
        return [doc.to_dict() for doc in docs]
    
    def trova_cliente_by_nome(self, nome: str) -> List[dict]:
        """
        Trova i clienti che corrispondono al nome specificato.
        """
        query = self.collection.where("nome", "==", nome)
        docs = query.stream()
        return [doc.to_dict() for doc in docs]