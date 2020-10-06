#Excercise2
"""Luodaan Person niminen luokka jossa määritellään title, name ja surname.
Luokassa ei ole metodia. Titlen pitäisi olla 'Dr', 'Mr', 'Mrs', 'Ms'. Muuten
nostetaan virheviestin ValueError title is not valid. Luodaan 2-3 oliota luokan
perusteella."""

class Person:
    def __init__(self,title,name,surname):
        if title in ["Dr","Mr","Mrs","Ms"]:
            self.title = title
        else:
            print("ValueError: " + f"{title} is not a valid title")
        self.name = name
        self.surname = surname


Dude1 = Person("Mr", "Mike", "Man")
print(Dude1.name)

Dude2 = Person("President", "Urho", "Kekkonen")
print(Dude2.name)

