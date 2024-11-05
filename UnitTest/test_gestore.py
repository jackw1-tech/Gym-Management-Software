import unittest
from unittest.mock import patch, MagicMock
from GestionePersonale.model.gestore import Gestore

class TestGestore(unittest.TestCase):
    @patch('GestionePersonale.model.gestore.db')
    def test_crea_gestore_firebase(self, mock_db):
        mock_collection = MagicMock() 
        mock_document = MagicMock()
        
        mock_db.collection.return_value = mock_collection
        mock_collection.document.return_value = mock_document
        
        gestore = Gestore("test_username", "test_password", "Nome", "Cognome")
        
        result = gestore.crea_gestore_firebase()
        self.assertTrue(result)
       
        mock_document.set.assert_called_once_with({
            'nome': 'Nome',
            'cognome': 'Cognome',
            'username': 'test_username',
            'password': 'test_password',
            'pt': [],
            'corsi': [],
            'pacchetti': []
        })

    @patch('GestionePersonale.model.gestore.db')
    def test_check_credentials_gestore(self, mock_db):
        user_data = {'username': 'test_username', 'password': 'test_password'}
        
        mock_document = MagicMock()
        mock_document.get.return_value.exists = True
        mock_document.get.return_value.to_dict.return_value = user_data
        
        mock_db.collection.return_value.document.return_value = mock_document
        
        gestore = Gestore("test_username", "test_password", "Nome", "Cognome")
        
        result = gestore.check_credentials_gestore("test_username", "test_password")
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()
