from abc import ABC, abstractmethod

# 1. Abstraction: The Blueprint
class Starship(ABC):
    def __init__(self, name, fuel):
        self.name = name
        self._fuel = fuel  # Protected attribute (Encapsulation)

    @abstractmethod
    def calculate_warp_speed(self):
        """Must be implemented by all subclasses"""
        pass

# 2. Inheritance & Polymorphism
class Freighter(Starship):
    def __init__(self, name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight
        self.inventory = []

    def calculate_warp_speed(self):
        # Polymorphism: Speed is affected by weight
        return 1000 / (self.cargo_weight + 1)

    # 5. Method Overloading (Python style)
    def load_cargo(self, item):
        if isinstance(item, str):
            self.inventory.append(item)
            print(f"Loaded item: {item}")
        elif isinstance(item, (int, float)):
            self.cargo_weight += item
            print(f"Increased weight by {item}. Total weight: {self.cargo_weight}")

class Fighter(Starship):
    def __init__(self, name, fuel, ammo):
        super().__init__(name, fuel)
        self.__ammo_count = ammo  # Private attribute (Encapsulation)

    # 3. Encapsulation: Property Getter/Setter
    @property
    def ammo(self):
        return self.__ammo_count

    @ammo.setter
    def ammo(self, value):
        if value < 0:
            print("Error: Ammo cannot be negative!")
        else:
            self.__ammo_count = value

    def calculate_warp_speed(self):
        # Polymorphism: Fixed high speed
        return 5000.0

    # 4. Operator Overloading (+)
    def __add__(self, other):
        if isinstance(other, Fighter):
            return Squadron([self, other])
        raise ValueError("A Fighter can only form a squadron with another Fighter.")

class Squadron:
    def __init__(self, ships):
        self.ships = ships

# --- TEST SUITE ---

# Test Abstraction: ship = Starship("Generic", 100) -> This would raise TypeError

# Test Inheritance & Polymorphism
falcon = Freighter(name="Millennium Falcon", fuel=100, cargo_weight=50)
tie = Fighter(name="TIE Advanced", fuel=100, ammo=10)

print(f"{falcon.name} Warp Speed: {round(falcon.calculate_warp_speed(), 2)}")
print(f"{tie.name} Warp Speed: {tie.calculate_warp_speed()}")

# Test Private Attributes & Properties
tie.ammo = 25          # Uses Setter
tie.ammo = -5          # Triggers validation in Setter
print(f"Current Ammo: {tie.ammo}") # Uses Getter

# Test Operator Overloading
tie2 = Fighter(name="TIE Interceptor", fuel=100, ammo=5)
squadron = tie + tie2  # Triggers __add__
print(f"Squadron formed with {len(squadron.ships)} ships.")

# Test Method Overloading (Type-based dispatch)
falcon.load_cargo("Kessel Spice") # Handled as string
falcon.load_cargo(500)            # Handled as number