class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model= usermodel
    def full_name (self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battry_size = battry_size

my_tesla = ElectricCar("Tesla", "model S", "85kw")
print(my_tesla.full_name())



# my_car = Car ("odi","bmw")
# print(my_car.brand)


