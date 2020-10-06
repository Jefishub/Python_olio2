class Opiskelija:
    def __init__(self, annettu_nimi, numero, tenttiarvosana, harjoitusarvosana):
        self.nimi = annettu_nimi
        self.opiskelijanumero = numero
        self.tenttiarvosana = tenttiarvosana
        self.harjoitusarvosana = harjoitusarvosana
        self.kokonais_arvosana = 0
    
    def tentti_suoritettu(self):
        if self.tenttiarvosana >= 3:
            return "Tentti on suoritettu. Onnea!"
        else:
            return "Olet epäonnistunut tentistä!"

    def harjoitus_suoritettu(self):
        if self.tenttiarvosana >= 2:
            return "Tentti on suoritettu. Onnea!"
        else:
            return "Olet epäonnistunut tentistä!"

    def vaihda_arvosana(self, uusi_numero):
        if uusi_numero <= 5 and uusi_numero >= 0:
            print(f"Vanha arvosana: {self.tenttiarvosana}")
            self.tenttiarvosana = uusi_numero
            print(f"Syötetään tenttiarvosanaksi {self.tenttiarvosana}")
        else:
            print("Ei kelvollinen arvosana")

    def laske_kokonais_arvosana(self):
        if self.tentti_suoritettu == 0 or self.harjoitusarvosana == 0:
            self.kokonais_arvosana = 0
            return self.kokonais_arvosana
        else:
            self.kokonais_arvosana = (1 + self.harjoitusarvosana + self.tenttiarvosana) / 3
            return round(self.kokonais_arvosana,2)


kurssilainen1 = Opiskelija("Johan Kämp", "212233", 3, 5)
kurssilainen2 = Opiskelija("Matti Korhonen", "562233", 2, 5)
print(kurssilainen1.tentti_suoritettu())
print(kurssilainen2.tentti_suoritettu())
print(kurssilainen1.harjoitus_suoritettu())
print(kurssilainen2.harjoitus_suoritettu())
print(kurssilainen2.tenttiarvosana)
kurssilainen2.vaihda_arvosana(5)
print(kurssilainen2.tenttiarvosana)
kurssilainen2.vaihda_arvosana(10)
print(kurssilainen2.tenttiarvosana)

print(f"Kokonaisarvosana on {kurssilainen2.laske_kokonais_arvosana()}")