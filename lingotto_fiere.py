lista_espossitori=[]
lista_stand=[]

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome



    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        print(nome)

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        infile = open(file_path, "r")
        for riga in infile:
            campo=riga.strip().split(",")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
