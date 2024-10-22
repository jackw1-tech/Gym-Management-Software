from GestionePalestra.model import corso
from GestionePalestra.model.abbonamento import Abbonamento
from pt import *

class Gestore:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.lista_clienti = []
        self.lista_pt = []

    def AggiungiAbbonamento(self, durata, prezzo, scadenza, listaclienti):
        return Abbonamento(durata, prezzo, scadenza, listaclienti)

    def aggiungiCorso(self, nome, descrizione):
        return corso(nome, descrizione)

    def AssegnaClientiPT(self, cliente, pt):
        # Logica per assegnare un cliente a un PT
        pt.clienti.append(cliente)

    def AssegnaCorsoPacchetto(self, corso, pacchetto):
        # Aggiunge un corso a un pacchetto
        pacchetto.corsi.append(corso)

    def AssegnaCorsoPT(self, corso, pt):
        # Assegna un corso a un PT
        pt.corsi.append(corso)

    def AssegnaPacchettoAdAbbonamento(self, abbonamento, pacchetto):
        # Logica per assegnare un pacchetto a un abbonamento
        abbonamento.pacchetti.append(pacchetto)

    def getListaClienti(self):
        return self.lista_clienti

    def getListaPT(self):
        return self.lista_pt

    def inserisciPT(self, nome, cognome, tariffa_oraria):
        pt = PT(nome, cognome, tariffa_oraria)
        self.lista_pt.append(pt)
        return pt