# Gym Management Software

## Introduzione
Questo progetto è un software gestionale per una palestra che offre una vasta gamma di servizi ai propri clienti. Il sistema permette la gestione delle iscrizioni, dei corsi, delle prenotazioni, della fatturazione e dei pagamenti.

## Requisiti
Assicurati di avere installato sul tuo sistema Python 3.x e pip, il gestore di pacchetti per Python.

## Creazione e Attivazione dell'Ambiente Virtuale
Apri il terminale e naviga nella directory del progetto utilizzando il comando `cd ....`. Una volta nella directory, crea l'ambiente virtuale eseguendo il comando `python3 -m venv venv`. Dopo aver creato l'ambiente, attivalo: su macOS e Linux utilizza `source venv/bin/activate`, mentre su Windows esegui `venv\Scripts\activate`. 

## Configurare firebase

1 - Creare un Progetto Firebase:
        Vai su Firebase Console.
        Clicca su "Aggiungi progetto" e segui le istruzioni per crearne uno nuovo.
2- Configurare Firestore:
        Una volta creato il progetto, vai alla sezione "Firestore Database" nel menu a sinistra.
        Clicca su "Crea database" e segui le istruzioni per configurare Firestore (puoi scegliere 
        la modalità in cui vuoi iniziare, ad esempio "Iniziare in modalità di test" per sviluppare e testare).
3- Scaricare il File di Credenziali:
        Dopo aver creato il progetto, vai alla sezione "Impostazioni progetto" (icona dell'ingranaggio in alto 
        a sinistra).
        Seleziona la scheda "Servizi account".
        Clicca su "Genera nuova chiave privata". Questo scaricherà un file JSON sul tuo computer.

4- Assicurati di essere tornato nella radice del progetto e installa le librerie necessarie eseguendo 
    `pip install python-dotenv firebase-admin`

5- Successivamente, crea un file `.env` nella radice del progetto e aggiungi il seguente contenuto, sostituendo il percorso con quello corretto per il tuo file JSON delle credenziali: `GOOGLE_APPLICATION_CREDENTIALS= .....`. 
Nella radice del progetto, è presente un file di esempio `.env.example`.

6- Infine, esegui l'applicazione con il comando `python3 main.py`.

## Struttura del Progetto
La struttura del progetto è la seguente:

    gym_management_software/    
    │ 
    ├── main.py # File principale dell'applicazione 
    ├── venv/ # Ambiente virtuale
    ├── .env # File di configurazione per le variabili d'ambiente 
    ├── .env.example # File che mostra come dovrebbe essere il .env 
    └── README.md # Documentazione del progetto

## Utilizzo
Una volta avviata l'applicazione, segui le istruzioni a schermo per accedere alle diverse funzionalità del software gestionale. Assicurati di avere una connessione a Internet attiva poiché il sistema utilizza Firebase per la gestione dei dati.