class Bike():
    def __init__(self, brand, displacement, hp):
        self.brand = brand
        self.__displacement = displacement
        self._hp = hp
        
    def set_displacement(self, cubic):
        if (cubic <= 0):
            print("Error: Negative value for displacement!")
        else:
            self.__displacement = cubic
            print("displacement was changed")
    
    def get_displacement(self):
        return self.__displacement
    
    def add_hp(self):
        self._hp += 1

    def add_hp_multi(self, addition):
        self._hp += addition
        
    def __str__(self):
        printout = f"Your bike from {self.brand} has {self._hp} hp and a displacement of {self.__displacement} cubic"
        return printout
    
class Harley(Bike):
    def __init__(self, brand, displacement, hp):
        self.brand = "Harley Davidson"
        self.__displacement = displacement
        self._hp = hp
        
    def __str__(self):
        printout = f"Your Harley Davidson has {self._hp} hp and a displacement of {self.__displacement} cubic"
        return printout
    
vehicle1 = Bike('Yamaha',10,200)
vehicle2 = Harley('Yamaha',8,250)

print(vehicle1)
print(vehicle2)