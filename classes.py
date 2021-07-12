"""
    Title: classes.py
    Description: This file demonstrates my understanding of the 
    classes section of python is easy course
"""


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    def repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False
        self._temp = 0
    
    def drive(self, drive = 1):
        self.isDriving = True
        self._temp = drive

    def stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += self._temp
        self._temp = 0

        if self.tripsSinceMaintenance >= 100:
            self.needsMaintenance = True

    def __str__(self) -> str:
        return "Car of make {} with model {} made in year {} with weight {} has made {} trips and {}".format(self.make, self.model, self.year, self.weight, self.tripsSinceMaintenance, "needs maintenance" if self.needsMaintenance == True else "does not need maintenance")

car1 = Cars("Mercedes", "s-class", 2018, "208kg")
car2 = Cars("Honda", "Accord", 2017, "125kg")
car3 = Cars("Toyota", "Venza", 2020, "476kg")

car1.drive(45)
car1.stop()
car2.drive(34)
car2.stop()
car3.drive(56)
car3.stop()
car3.drive(45)
car3.stop()
car2.drive(78)
car2.stop()
car2.drive(12)
car2.stop()
car3.drive(4)
car3.stop()
car2.drive(2)
car2.stop()
car2.drive(34)
car2.stop()
car3.drive(89)
car3.stop()
car2.drive(1)
car2.stop()

print(car1)
print(car2)
print(car3)
