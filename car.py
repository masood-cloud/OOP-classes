class car:
    ##when you declare a variable outside of a method, it’s treated as a class variable'
    wheels = 4

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12



    # Controlled access
    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problem")
        self._voltage = volts


    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop")
        del self._voltage


my_car = car("yellow", "beetle", 1978)

print(f"my car color is {my_car.color}")

"""You can also create instance variables outside of .__init__(), but it’s not a best practice as their scope is often confusing"""

my_car.wheels = 4
print(f"it has {my_car.wheels} wheels")

print(f"The model is {my_car.model}")

print(f"{my_car.year} is the year of my car")

print(f"my car uses {my_car._voltage} volt")
my_car._voltage = 6

print(f"my car now use {my_car._voltage} volts")

del my_car.voltage
