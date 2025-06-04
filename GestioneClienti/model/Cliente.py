from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List, Dict

from GestioneClienti.model import Abbonamento

@dataclass
class SchedaCliente:
    id: str = None
    peso: float = 0.0
    altezza: float = 0.0
    massa_muscolare: float = 0.0
    massa_grassa: float = 0.0
    bmi: float = 0.0
    misure: dict[str, float] = field(default_factory=dict)
    note: str = ""
    data_rilevazione: date = date.today()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "peso": self.peso,
            "altezza": self.altezza,
            "massa_muscolare": self.massa_muscolare,
            "massa_grassa": self.massa_grassa,
            "bmi": self.bmi,
            "misure": self.misure,
            "note": self.note,
            "data_rilevazione": self.data_rilevazione.isoformat()
        }
    @classmethod
    def from_dict(cls, data: dict) -> 'SchedaCliente':
        return cls(
            id=data.get("id"),
            peso=data.get("peso", 0.0),
            altezza=data.get("altezza", 0.0),
            massa_muscolare=data.get("massa_muscolare", 0.0),
            massa_grassa=data.get("massa_grassa", 0.0),
            bmi=data.get("bmi", 0.0),
            misure=data.get("misure", {}),
            note=data.get("note", ""),
            data_rilevazione=date.fromisoformat(data.get("data_rilevazione", date.today().isoformat()))
        )
    
class Sesso(Enum):
    MASCHIO = "Maschio"
    FEMMINA = "Femmina"
    ALTRO = "Altro"

@dataclass
class Cliente:
    id: str = None
    nome: str = ""
    cognome: str = ""
    data_nascita: date = date.today()
    email: str = ""
    telefono: str = ""
    sesso: Sesso = Sesso.MASCHIO
    scheda: SchedaCliente = None
    abbonamento: Abbonamento = None
    foto: str = ""
    certificatoMedico: str = ""
    #pt_ids: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "data_nascita": self.data_nascita.isoformat() if isinstance(self.data_nascita, date) else self.data_nascita,
            "sesso": self.sesso.value if isinstance(self.sesso, Sesso) else self.sesso,
            "email": self.email,
            "telefono": self.telefono,
            "scheda": self.scheda.to_dict() if self.scheda else {},
            "abbonamento": self.abbonamento.to_dict() if self.abbonamento else {},
            "foto": self.foto,
            "certificatoMedico": self.certificatoMedico,
            #"pt_ids": self.pt_ids
        }

    @classmethod
    def from_dict(cls, id: str, data: dict) -> 'Cliente':
        # 1) Recupero e converto data_nascita
        raw = data.get("data_nascita", None)
        if isinstance(raw, str):
            try:
                data_nasc = date.fromisoformat(raw)
            except Exception:
                data_nasc = None
        elif hasattr(raw, "date"):
            data_nasc = raw.date()
        else:
            data_nasc = None

        # 2) Reconstruisco scheda e abbonamento (se li usi)
        scheda_obj = None
        if data.get("scheda"):
            scheda_obj = SchedaCliente.from_dict(data["scheda"])

        abbonamento_obj = None
        if data.get("abbonamento"):
            abbonamento_obj = Abbonamento.from_dict(data["abbonamento"])

        return cls(
            id=id,
            nome=data.get("nome", ""),
            cognome=data.get("cognome", ""),
            data_nascita=data_nasc,
            email=data.get("email", ""),
            telefono=data.get("telefono", ""),
            scheda=scheda_obj,
            abbonamento=abbonamento_obj,
            foto=data.get("foto", ""),
            certificatoMedico=data.get("certificatoMedico", ""),
            #pt_ids=data.get("pt_ids", [])
        )
    
