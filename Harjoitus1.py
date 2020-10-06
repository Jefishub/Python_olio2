class Car:
    """Car class

    Args:
        merkki (string): Auton merkki, esim. Audi, Toyota...
        color (string): Auton väri
        malli (string): Auton malli
        distance_drived (int): Ajetut kilometrit (km)
        price (int): Auton hinta (euros)
    """  
    
    def __init__(self,merkki,color,malli,distance_drived,price):    
        self.merkki = merkki
        self.color = color
        self.malli = malli
        self.distance_drived = distance_drived #in km
        self.price = price #in euros

    
    def __str__(self):
        return f"{self.color} {self.merkki} {self.malli} car with {self.distance_drived} km drived costs {self.price} euros."


myNewCar = Car("Audi","Red","A3",50000,10500)
mySecondCar = Car("Toyota","Black","Avensis",30000,20500)
myThirdCar = Car("Tesla", "White", "Model S", 10000, 67000)

print(myNewCar)
print(mySecondCar)
print(myThirdCar)
print(Car.__doc__)