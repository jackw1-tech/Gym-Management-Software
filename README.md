# Gym Management Software

## Introduzione
Questo progetto è un software gestionale per una palestra che offre una vasta gamma di servizi ai propri clienti. Il sistema permette la gestione delle iscrizioni, dei corsi, delle prenotazioni, della fatturazione e dei pagamenti.

## Requisiti
Assicurati di avere installato sul tuo sistema Python 3.x e pip, il gestore di pacchetti per Python.

## Creazione e Attivazione dell'Ambiente Virtuale
Apri il terminale e naviga nella directory del progetto utilizzando il comando `cd ....`. Una volta nella directory, crea l'ambiente virtuale eseguendo il comando `python3 -m venv venv`. Dopo aver creato l'ambiente, attivalo: su macOS e Linux utilizza `source venv/bin/activate`, mentre su Windows esegui `venv\Scripts\activate`. 

Installa le librerie necessarie eseguendo `pip install python-dotenv firebase-admin`. Successivamente, crea un file `.env` nella radice del progetto e aggiungi il seguente contenuto, sostituendo il percorso con quello corretto per il tuo file JSON delle credenziali: `GOOGLE_APPLICATION_CREDENTIALS= .....`. 

Infine, esegui l'applicazione con il comando `python3 app.py`.

## Struttura del Progetto
La struttura del progetto è la seguente:

