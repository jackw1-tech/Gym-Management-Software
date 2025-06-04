from dataclasses import dataclass
from datetime import date
from enum import Enum

@dataclass
class Pacchetto:
    id: str = None
    nome: str = ""
    lista_corsi: list[str] = None
    prezzo: float = 0.0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "lista_corsi": self.lista_corsi
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Pacchetto':
        return cls(
            id=data.get("id"),
            nome=data.get("nome", ""),
            lista_corsi=data.get("lista_corsi", [])
        )

@dataclass
class Corso:
    id: str = None
    nome: str = ""
    descrizione: str = ""
    durata: int = 0
    costo: float = 0.0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "durata": self.durata,
            "costo": self.costo
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Corso':
        return cls(
            id=data.get("id"),
            nome=data.get("nome", ""),
            descrizione=data.get("descrizione", ""),
            durata=data.get("durata", 0),
            costo=data.get("costo", 0.0)
        )

class StatoAbbonamento(Enum):
    ATTIVO = "ATTIVO"
    SCADUTO = "SCADUTO"
    SOSPESO = "SOSPESO"
    ANNULLATO = "ANNULLATO"

@dataclass
class Abbonamento:
    id: str = None
    pacchettoCorso: Pacchetto = None
    data_inizio: date = date.today()
    data_fine: date = date.today()
    prezzo: float = 0.0
    stato: StatoAbbonamento = StatoAbbonamento.ATTIVO
    id_cliente: str = None
    saldato: bool = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "pacchetto_corso": self.pacchettoCorso.to_dict() if self.pacchettoCorso else None,
            "data_inizio": self.data_inizio.isoformat(),
            "data_fine": self.data_fine.isoformat(),
            "prezzo": self.prezzo,
            "stato": self.stato.value,
            "id_cliente": self.id_cliente,
            "saldato": self.saldato
        }
    @classmethod
    def from_dict(cls, data: dict) -> 'Abbonamento':
        def parse_date_safe(val):
            try:
                if isinstance(val, str) and val:
                    return date.fromisoformat(val)
            except Exception:
                pass
            return date.today()

        return cls(
            id=data.get("id"),
            pacchettoCorso=Pacchetto.from_dict(data.get("pacchetto_corso", {})) if data.get("pacchetto_corso") else None,
            data_inizio=parse_date_safe(data.get("data_inizio")),
            data_fine=parse_date_safe(data.get("data_fine")),
            prezzo=data.get("prezzo", 0.0),
            stato=StatoAbbonamento(data.get("stato", StatoAbbonamento.ATTIVO.value)),
            id_cliente=data.get("id_cliente"),
            saldato=data.get("saldato", False)
        )



