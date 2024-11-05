import unittest
from unittest.mock import patch, MagicMock
from GestionePalestra.model.corso import corso

class TestCorso(unittest.TestCase):

    @patch('GestionePalestra.model.corso.db')
    def test_recupera_dettagli_corso(self, mock_db):
        expected_data = {
            'nome': 'Test Corso',
            'descrizione': "Questo è un corso di test.",
            'pt_assegnato': []
        }
        mock_document = MagicMock()
        
        # Simulo il comportamento del metodo get del documento
        mock_document.get.return_value.exists = True
        # Simulo il comportamento del metodo to_dict del documento
        mock_document.get.return_value.to_dict.return_value = expected_data
       
        # Imposto il comportamento del mock per la collezione e il documento
        mock_db.collection.return_value.document.return_value = mock_document

        corso_instance = corso("Test Corso", "Questo è un corso di test.")
        result = corso_instance.recupera_dettagli_corso("test_corso_id")
       
       
        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()