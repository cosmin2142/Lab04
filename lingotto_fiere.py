from stand import Stand, StandPreseExtra, StandPremium
from espositore import Espositore
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.lista_stand = []
        self.lista_espositori = []


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
            riga=riga.strip()
            campi=[]
            for campo in riga.split(","):
                campi.append(campo.strip())
                codice=campi[0]
            if codice.startswith('ST'):
                superficie = campi[1]
                padiglione = campi[2]
                prezzo_base = campi[3]

                if len(campi) == 4:
                    stand = Stand(codice, superficie, padiglione, prezzo_base)
                elif len(campi) == 5:
                    quinto_campo = campi[4]
                    try:
                        num_prese = int(quinto_campo)
                        stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, num_prese)
                    except ValueError:
                        stand = StandPremium(codice, superficie, padiglione, prezzo_base, quinto_campo)
                if stand not in self.lista_stand:
                    self.lista_stand.append(stand)

            elif codice.startswith('ES'):
                nome = campi[1]
                cognome = campi[2]
                espositore = Espositore(codice, nome, cognome)

                if espositore not in self.lista_espositori:
                    self.lista_espositori.append(espositore)

    def trova_stand(self, codice_stand):
        for s in self.lista_stand:
            if s.codice == codice_stand:
                return s
        return None

    def trova_espositore(self, codice_espositore):
        for e in self.lista_espositori:
            if e.codice == codice_espositore:
                return e
        return None


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand = self.trova_stand(codice_stand)
        espositore = self.trova_espositore(codice_espositore)

        if not stand:
            raise ValueError(f"Lo stand con codice {codice_stand} non esiste.")
        if not espositore:
            raise ValueError(f"L'espositore con codice {codice_espositore} non esiste.")
        if not stand.disponibile:
            raise ValueError(f"Lo stand {codice_stand} non è disponibile.")
        if espositore.stand is not None:
            raise ValueError(
                f"L'espositore {codice_espositore} è già associato a un altro stand ({espositore.stand.codice}).")
        stand.espositore = espositore
        espositore.stand = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for e in self.lista_espositori:
            print(e)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        stand_ordinati=sorted(self.lista_stand)
        return stand_ordinati
