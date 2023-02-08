class Balkezesek:

    def __init__(self, sor):
        darabolt = sor.split(";")
        self.nev = darabolt[0]
        self.elso = darabolt[1]
        self.utolso = darabolt[2]
        self.suly = int(darabolt[3])
        self.magassag = int(darabolt[4])
