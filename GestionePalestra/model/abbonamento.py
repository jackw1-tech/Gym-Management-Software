class Abbonamento:
    def __init__(self, durata, prezzo, scadenza):
        self.durata = durata  # Durata in mesi
        self.prezzo = prezzo  # Prezzo dell'abbonamento
        self.listaPacchetti = []  # Lista dei pacchetti disponibili
        self.scadenza = scadenza

    def getDurata(self):
        return self.durata

    def getPrezzo(self):
        return self.prezzo

    def setDurata(self, durata):
        self.durata = durata

    def inserisciPrezzo(self, prezzo):
        self.prezzo = prezzo

    def getPacchettoScelto(self):
        return self.listaPacchetti
    
    def getScadenza(self):
        return self.scadenza