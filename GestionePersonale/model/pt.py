
class PT:
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
        self.clienti = []
        self.corsi = []

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getStipendio(self):
        return self.stipendio

    def getListaClienti(self):
        return self.clienti

    def getListaCorsi(self):
        return self.corsi

    def inserisciNome(self, nome):
        self.nome = nome

    def inserisciCognome(self, cognome):
        self.cognome = cognome

    def inserisciStipendio(self, stipendio):
        self.stipendio = stipendio

   