from abc import ABC, abstractmethod
from typing import List

class BaseDAO(ABC):

    @abstractmethod
    def fetch_all(self, id):
        pass

    @abstractmethod
    def fetch_by_id(self, id):
        pass

    @abstractmethod
    def create_cliente(self, cliente):
        """
        Crea un nuovo Cliente nel database.

        :param cliente: Oggetto Cliente da inserire.
        """
        pass

    @abstractmethod
    def update(self, id, obj):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def fetch_abbonamenti_by_cliente_id(self, cliente_id: str) -> List[dict]:
        pass

    @abstractmethod
    def trova_cliente_by_nome(self, nome: str) -> List[dict]:
        """
        Trova i clienti che corrispondono al nome specificato.

        :param nome: Nome del cliente da cercare.
        :return: Lista di dizionari contenenti i dati dei clienti trovati.
        """
        pass