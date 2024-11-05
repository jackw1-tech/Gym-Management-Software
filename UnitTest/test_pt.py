import unittest
from unittest.mock import patch, MagicMock
from GestionePersonale.model.pt import PT

class TestPT(unittest.TestCase):
    @patch('GestionePersonale.model.pt.db')
    def test_rimuovi_corso_da_pt_success(self, mock_db):
        mock_pt_ref = mock_db.collection.return_value
        
        mock_pt_ref.stream.return_value = [
            MagicMock(id="pt_test_id", to_dict=lambda: {'corsi': ["corso_test_id", "corso2"]})
        ]
        
        PT.rimuovi_corso_da_pt("corso_test_id")

        mock_pt_ref.document.assert_called_once_with("pt_test_id")
        
        mock_pt_ref.document("pt_test_id").update.assert_called_once_with({
            'corsi': ["corso2"] 
        })

if __name__ == '__main__':
    unittest.main()
