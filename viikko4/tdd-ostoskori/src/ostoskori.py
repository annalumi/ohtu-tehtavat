
from ostos import Ostos
from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._ostokset])
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum([ostos.hinta() for ostos in self._ostokset])
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        nimet = []
        for ostos in self._ostokset:
            nimet.append(ostos.tuotteen_nimi())
        
        if lisattava.nimi() in nimet:
            [ostos.muuta_lukumaaraa(1) for ostos in self._ostokset if ostos.tuotteen_nimi() == lisattava.nimi()]
        else:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        [ostos.muuta_lukumaaraa(-1) for ostos in self._ostokset if ostos.tuotteen_nimi() == poistettava.nimi()]
        self._ostokset = [ostos for ostos in self._ostokset if ostos.lukumaara() > 0]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset=[]

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on