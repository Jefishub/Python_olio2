#Excercise 3
"""Meillä on luokka nimeltä Person. Person luokassa on vain yksi kenttä pets,
jossa tallennetaan henkilön eläimen nimeä listana. Eläimet ei tarvitse
määritellä kun luodaan oliota. Eläimiä voidaan lisätä myöhemmin luokan
add_pet metodin avulla."""

class Person:
    def __init__(self,pets=[]):
        self.pets = pets

    def add_pet(self, new_pet):
        self.pets.append(new_pet)


janne = Person()
print("Jannen eläimet: ", janne.pets)
helena = Person()
print("Helenan eläimet: ", helena.pets)

janne.add_pet("cat")
janne.add_pet("dog")

print("Jannen eläimet: ", janne.pets)
print("Helenan eläimet: ", helena.pets) # -> "Helenan eläimet:  ['cat', 'dog']", MIKSI ???? Helenalla ei pitäisi olla eläimiä...