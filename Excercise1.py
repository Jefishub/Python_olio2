#Toimeksianto
"""Yritetään tehdä on henkilöstöluettelo. Jokaisessa henkilössä nimi, sukunimi,
syntymäpäivä, sähköposti, puhelinnumero ja kotiosoite. Tee tämän
implementaatiota ja luo muutama oliota.

Lisähaaste: Syntymäpäivä voi määritellä datetime muodossa ja kirjoita
metodin joka laske henkilön iän."""


from datetime import *

class Henkilo_luettelo:
    def __init__(self,nimi,sukunimi,syntpvm,email="",puhelinnumero="",kotiosoite=""):
        self.nimi = nimi
        self.sukunimi = sukunimi
        self.syntpvm = syntpvm
        self.email = email
        self.puhelinnumero = puhelinnumero
        self.kotiosoite = kotiosoite

    def ika(self):
        today = date.today()
        age = today.year - self.syntpvm.year

        if today < date(today.year, self.syntpvm.month, self.syntpvm.day):
            age -= 1
        
        return age
        


man1 = Henkilo_luettelo("Jorma", "Jormakka", date(1985,2,23))
print(date.today())
print(man1.syntpvm)
print(man1.ika())