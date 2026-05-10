#Python OOP
#Encapsulation-->Hiding internal data of a class and controlling access via getter and setter methods to protect data integrity.
#Abstraction-->
#Inheritance-->Mechanism to create new classes (child) from existing classes (parent), enabling code reuse and extension.
#Polymorphism-->Ability to define methods with the same name but different implementations (method overriding and method overloading).
#Constructor (__init__): A special method that initializes new objects automatically when created.
#Magic Methods: Special methods in Python with double underscores (__method__) automatically invoked by Python (e.g., __init__, __str__, __add__).

class NameOfClass:
    # 1. The Constructor (Initializing data)
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    # 2. An Instance Method (Defining behavior)
    def some_method(self):
        # Logic goes here
        return f"Doing something with {self.attribute1}"
class Dog:
    # The "Constructor" - this sets up the initial data
    def __init__(self, name, breed):
        self.name = name   # Attribute
        self.breed = breed # Attribute

    # A Method (a function that belongs to a class)
    def bark(self):
        print(f"{self.name} says: Woof!")
        
#Instance Variable
#These are variables that belong to a specific object. Every time you create a new object, it gets its own copy of these variables.
class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Luna")

print(dog1.name) # Output: Buddy
print(dog2.name) # Output: Luna

#Static Variable
#These are variables that belong to the Class itself. All objects created from that class share the exact same piece of data. If you change it in one place, it changes for everyone.

class Dog:
    species = "Canine"  # Static (Class) variable

    def __init__(self, name):
        self.name = name # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Luna")

print(dog1.species) # Output: Canine
print(dog2.species) # Output: Canine

# If we change the class variable...
Dog.species = "Wolf"

print(dog1.species) # Output: Wolf (It changed for Buddy too!)

#Inheritance
#Inheritance is one of the core pillars of OOP. It allows one class (the Child) to derive or "inherit" all the attributes and methods from another class (the Parent).
# The Parent Class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# The Child Class
class Dog(Animal):
    def bark(self):
        print("Woof woof!")

# Usage
my_dog = Dog()
my_dog.speak() # Inherited from Animal
my_dog.bark()  # Defined in Dog

#The super() Function
#It is used to call a method of a parent class in a child class
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        # super() calls the Parent's __init__
        super().__init__(name) 
        self.grade = grade

s1 = Student("Alice", "A")
print(s1.name)  # From Person
print(s1.grade) # From Student

#Polymorphism
#1)Method Overriding
#If a child class defines a method with the same name as a parent class method, the child's version overrides the parent's.
class Bird:
    def fly(self):
        print("The bird is flying")

class Penguin(Bird):
    def fly(self):
        # Overriding the parent method
        print("Penguins cannot fly, they swim!")

p = Penguin()
p.fly() # Output: Penguins cannot fly, they swim!

#2) Method Overloading
#Python does not support traditional method overloading However, because Python is dynamically typed and incredibly flexible, we can achieve the same behavior using a few clever techniques.
class Calculator:
    def add(self, a, b, c = 0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))      # Works with 2 arguments
print(calc.add(5, 10, 20))  # Works with 3 arguments

#3) Operator Overloading
#Operator Overloading is about redefining how standard operators (like +, -, *, or <) behave when used with your own custom objects.
#This is achieved by implementing special methods called Magic Methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the str() function for pretty printing
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(3, 1)

# This calls v1.__add__(v2) under the hood
v3 = v1 + v2

print(v3)  # Output: Vector(5, 5)


        
