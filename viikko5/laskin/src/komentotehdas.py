class Summa:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        return self.sovellus.plus(self.io())

class Erotus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        return self.sovellus.miinus(self.io())

class Nollaus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        return self.sovellus.nollaa()



