"""
Pickle the following class


"""

class Car:
    cars_created = 0
    def __init__(self, num_tires = 2, color = "red", gas=True):
        self.num_tires = num_tires
        self.color = color
        self.gas = gas
    
    def is_gas(self):
        return self.gas

    def honk_horn(self):
        print("HONK HONK")
    
    def can_drive(self):
        if self.num_tires == 4:
            return True
        return False

## pickle the actual class Car 



my_car = Car(4, 'blue', True)
# pickle your instance of the car


