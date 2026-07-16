# Basic class and object
class Car:
    total_car = 0
    # is ki waja say hum perameter pass kr sakta hain
    # self. ka matlab hai class ka under ka veriable
    # or jo bracket ka under hain inha perameter bota hai
    # ye user ne tub dia jub wo object bana raha tha
    # class ka under ka access lena hai to self. likhna para ga

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def fuel_type(self):
        return "Petrol or Diesel"
# staticmethod me self ki zourarat nhi
# is ko class access kr sakti hai object ni

    @staticmethod
    def gernel_description():
        return "Cars are Beautifull"

    # is say hum overwrite nhi kr sakta
    @property
    def model(self):
        return self.__model
# class method and self

    def ful_name(self):
        return f"{self.brand} {self.__model}"
# inheritance (virasat)


class ElectricCar(Car):
    def __init__(self, brand, __model, battery_size):
        super().__init__(brand, __model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
# Encapsulation (is me hum method say kesi be item ko access kr sakta hain wasa nhi)


# my_car ka under ek object hai car
my_car = Car("Honda", "Corolla")
my_electric = ElectricCar("Tesla", "Model Y", "80kwh")
print(my_car.brand)
print(my_car.model)
print(my_car.ful_name())
print(my_electric.ful_name())
print(my_electric.fuel_type())
print(Car.total_car)
print(my_electric.gernel_description())
print(isinstance(my_electric, ElectricCar))


# Multiple Inheritance → 1 child, multiple parents
class Battery:
    def battery_info(self):
        return "This Is best battery"


class Engine:
    def engine_info(self):
        return "This is best Engine"

# child


class Electric_car(Battery, Engine, Car):
    pass


# object
my_tesla = Electric_car("Tesla", "Model Y")
print(my_tesla.engine_info())
print(my_tesla.battery_info())
