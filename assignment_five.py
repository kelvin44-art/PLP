# PART 1: Smartphone Classes with Inheritance
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False
        self.apps = []
    
    def power_toggle(self):
        self.is_on = not self.is_on
        return f"{self.brand} {self.model} is now {('on' if self.is_on else 'off')}"
    
    def install_app(self, app):
        if self.is_on:
            self.apps.append(app)
            return f"Installed {app}"
        return "Phone is off. Cannot install apps."
    
    def get_info(self):
        return f"{self.brand} {self.model}, {self.storage}GB"


class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, android_version):
        super().__init__(brand, model, storage)
        self.android_version = android_version
    
    def get_info(self):
        return f"{super().get_info()}, Android {self.android_version}"


class IPhone(Smartphone):
    def __init__(self, model, storage, ios_version):
        super().__init__("Apple", model, storage)
        self.ios_version = ios_version
    
    def get_info(self):
        return f"{super().get_info()}, iOS {self.ios_version}"


# Demonstrate Smartphone classes
def test_smartphones():
    print("=== SMARTPHONE CLASS DEMO ===")
    android = AndroidPhone("Samsung", "Galaxy S21", 128, 13)
    iphone = IPhone("iPhone 14", 256, 16)
    
    print(android.get_info())
    print(iphone.get_info())
    
    print(android.power_toggle())
    print(android.install_app("Maps"))
    print(iphone.install_app("Safari"))  # Will fail because phone is off
    print(iphone.power_toggle())
    print(iphone.install_app("Safari"))


# PART 2: Vehicle Classes with Polymorphism
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        return f"{self.name} is moving"


class Car(Vehicle):
    def move(self):
        return f"🚗 {self.name} is driving at {self.speed} mph"


class Boat(Vehicle):
    def move(self):
        return f"⛵ {self.name} is sailing at {self.speed} mph"


class Plane(Vehicle):
    def move(self):
        return f"✈️ {self.name} is flying at {self.speed} mph"


# Demonstrate Vehicle polymorphism
def test_vehicles():
    print("\n=== VEHICLE POLYMORPHISM DEMO ===")
    vehicles = [
        Car("Tesla", 75),
        Boat("Sailboat", 20),
        Plane("Boeing", 550)
    ]
    
    for vehicle in vehicles:
        print(vehicle.move())


# Run demonstrations
if __name__ == "__main__":
    test_smartphones()
    test_vehicles()