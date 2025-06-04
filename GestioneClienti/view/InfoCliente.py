import customtkinter as ctk
from PIL import Image

class InfoClientePage(ctk.CTkFrame):
    def __init__(self, master, cliente, controller, back_callback):
        """
        master: riferimento al MainView
        cliente: oggetto cliente da visualizzare
        back_callback: funzione da chiamare per tornare alla pagina precedente
        """
        super().__init__(master)

        self.cliente = cliente
        self.controller = controller
        self.back_callback = back_callback

        self.abbonamenti = self.controller.get_abbonamenti_by_cliente_id(cliente.id)

        # Layout a griglia (2 righe, 1 colonna)
        self.grid_rowconfigure(0, weight=0)  # riga titolo
        self.grid_rowconfigure(1, weight=1)  # riga contenuto
        self.grid_columnconfigure(0, weight=1)

        # Titolo della pagina
        title_label = ctk.CTkLabel(
            self,
            text=f"Informazioni Cliente: {cliente.nome}",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=0, column=0, pady=(10, 5), sticky="n")

        # Bottone "Indietro"
        back_button = ctk.CTkButton(
            master=self,
            text="Indietro",
            width=100,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=self.back_callback
        )
        back_button.grid(row=0, column=0, pady=(10, 5), padx=(10, 0), sticky="w")

        # Contenuto delle informazioni del cliente
        self.content_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#3a3a4d",
            width=600,
            height=400
        )
        self.content_frame.grid_rowconfigure(0, weight=1)  # Permette alla riga di espandersi
        self.content_frame.grid_columnconfigure(0, weight=1)  # Permette alla colonna di espandersi
        self.content_frame.grid(row=1, column=0, padx=20, pady=(5, 20), sticky="nsew")

        # Frame per le informazioni del cliente
        info_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=10,
            fg_color="#44445a"
        )
        info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        info_frame.grid_rowconfigure(0, weight=1)  # Permette alla riga di espandersi
        info_frame.grid_columnconfigure(0, weight=1)  # Permette alla colonna di espandersi

        # Etichette per le informazioni del cliente
        
        labels = [
            ("Nome:", cliente.nome),
            ("Cognome:", cliente.cognome),
            ("Email:", cliente.email),
            ("Telefono:", cliente.telefono),
            ("Data di Nascita:", cliente.data_nascita.strftime('%d/%m/%Y') if hasattr(cliente.data_nascita, 'strftime') else str(cliente.data_nascita)),
            ("Sesso:", cliente.sesso.value if hasattr(cliente.sesso, 'value') else str(cliente.sesso)),
        ]

        for idx, (label_text, value) in enumerate(labels):
            label = ctk.CTkLabel(
            info_frame,
            text=label_text,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#cccccc"
            )
            label.grid(row=idx, column=0, sticky="w", padx=(10, 5), pady=5)

            value_label = ctk.CTkLabel(
            info_frame,
            text=value,
            font=ctk.CTkFont(size=16),
            text_color="#ffffff"
            )
            value_label.grid(row=idx, column=1, sticky="w", padx=(0, 10), pady=5)

        # Sezione per gli abbonamenti
        SezioneAbbonamento(
            master=self.content_frame,
            abbonamenti=self.abbonamenti
        ).grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 20))

class AbbonamentoCard(ctk.CTkFrame):
    def __init__(self, master, abbonamento):
        super().__init__(master)
        self.abbonamento = abbonamento

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Mostra le specifiche dell'abbonamento in un frame orizzontale
        specifiche_frame = ctk.CTkFrame(
            master=self,
            corner_radius=8,
            fg_color="#44445a"
        )
        specifiche_frame.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        specifiche_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        specifiche_frame.grid_rowconfigure(0, weight=1)


        self.id_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"ID: {self.abbonamento.id}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff"
        )
        self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.data_inizio_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Inizio: {self.abbonamento.data_inizio.strftime('%d/%m/%Y')}",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.data_inizio_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.data_fine_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Fine: {self.abbonamento.data_fine.strftime('%d/%m/%Y')}",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.data_fine_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.prezzo_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Prezzo: {self.abbonamento.prezzo} €",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.prezzo_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        self.stato_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Stato: {self.abbonamento.stato.value}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff"
        )
        self.stato_label.grid(row=0, column=4, padx=10, pady=(5, 0), sticky="w")

class SezioneAbbonamento(ctk.CTkFrame):
    def __init__(self, master, abbonamenti=None):
        super().__init__(master, corner_radius=10)

        self.grid_rowconfigure(0, weight=1)

        self.abbonamenti = abbonamenti
        titolo = ctk.CTkLabel(
            master=self,
            text="Abbonamenti",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ffffff"
        )

        titolo.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

        if not self.abbonamenti:
            self.abbonamenti = []
            # Se non ci sono abbonamenti, mostro un messaggio
            no_abbonamenti_label = ctk.CTkLabel(
                master=self,
                text="Nessun abbonamento disponibile.",
                font=ctk.CTkFont(size=16),
                text_color="#ffffff"
            )
            no_abbonamenti_label.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="n")

        for abbonamento in self.abbonamenti:
            card = AbbonamentoCard(master=self, abbonamento=abbonamento)
            card.grid(row=self.grid_size()[1], column=0, padx=10, pady=5, sticky="ew")
        
        aggiungi_abbonamento_button = ctk.CTkButton(
            master=self,
            text="Aggiungi Abbonamento",
            width=200,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            #command=self.aggiungi_abbonamento
        )
        aggiungi_abbonamento_button.grid(row=self.grid_size()[1], column=0, padx=10, pady=(5, 10), sticky="e")