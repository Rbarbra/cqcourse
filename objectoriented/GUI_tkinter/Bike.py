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

        
harley = Bike("Harley Davidson",500,80)
print(harley.brand)
print(harley._hp)
# print(harley.__displacement)
print(harley.get_displacement())

harley.add_hp()
print(harley._hp)
harley.add_hp_multi(20)
print(harley._hp)

harley.set_displacement(-500)
harley.set_displacement(600)
print(harley.get_displacement())

print(harley)