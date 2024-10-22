class corso:
    def __init__(self, nome, descrizione):
        self.nome = nome  # Nome del corso
        self.descrizione = descrizione  # Descrizione del corso
        self.pt_assegnato = None  # PT (Personal Trainer) assegnato al corso

    def getNome(self):
        return self.nome

    def getDescrizione(self):
        return self.descrizione

    def getPTAssegnato(self):
        return self.pt_assegnato

    def setNome(self, nome):
        self.nome = nome

    def setDescrizione(self, descrizione):
        self.descrizione = descrizione

    def assegnaPT(self, pt):
        self.pt_assegnato = pt