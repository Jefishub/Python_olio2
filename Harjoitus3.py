class Cook:
    def __init__(self,name,emplyment_typ,salary_per_hour):
        self.name = name
        self.emplyment_typ = emplyment_typ
        self.salary_per_hour = salary_per_hour

    def printname(self):
        print(self.name)


class ChineseCook(Cook):
        pass



kokki1 = ChineseCook("Jorma", "full time", 14)

kokki1.printname()
print(kokki1.name)
print(kokki1.salary_per_hour)