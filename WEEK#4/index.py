        self.storage = storage
        self.battery_life = battery_life
        
    def make_call(self, number):
        print(f"Calling {number} from {self.model}")
        
    def send_message(self, number, message):
        print(f"Sending '{message}' to {number} from {self.model}")
        
class SmartphonePro(Smartphone):
    def facial_recognition(self):
        print(f"{self.model} unlocking with facial recognition")
        
    def wireless_charging(self):
        print(f"{self.model} charging wirelessly.")
phone1 = SmartphonePro("TechBrand", "X100", "128GB", "24 hours")
phone1.make_call("+1234567890")
phone1.facial_recognition()


class Vehicle:
    def move(self):
        pass  # Abstract method (can be overridden)

class Car(Vehicle):
    def move(self):
        print("Driving on roads ")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()