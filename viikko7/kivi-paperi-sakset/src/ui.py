from kps import KPS, KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly

class UI:
    def __init__(self):
        self._valinnat = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }

    def _valitse(self, valinnat):
        valinnat.pelaa()


    def start(self):
        while True:
            print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
            )

            vastaus = input()

            if vastaus in "abc":
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                self._valitse(self._valinnat[vastaus])

            else:
                break