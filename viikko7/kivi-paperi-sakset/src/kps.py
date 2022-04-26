from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly

class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            print("Kiitos!")
            print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

# luokka perii luokan KPS
class KPSPelaajaVsPelaaja(KPS):
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto

class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        toinen_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {toinen_siirto}")

        return toinen_siirto

class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)