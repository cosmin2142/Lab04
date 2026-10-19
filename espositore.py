class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.codice == other.codice
        else:
            return False

    def __str__(self):
        stand_info = f"Stand: {self.stand.codice}" if self.stand else "Nessuno stand assegnato"
        return f"[{self.codice}] {self.nome} {self.cognome} - {stand_info}"

    def __repr__(self):
        return self.__str__()