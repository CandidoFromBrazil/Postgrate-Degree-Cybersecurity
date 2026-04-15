class Dog:
    # The __init__ method is the "constructor" 
    # It initializes the object's attributes
    def __init__(self, name, breed):
        self.name = name   # Attribute
        self.breed = breed # Attribute

    # A method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

    # Another method using attributes
    def get_info(self):
        return f"{self.name} is a {self.breed}."

# --- Using the Class ---

# 1. Create an "instance" of the class (an object)
my_dog = Dog(name="Buddy", breed="Golden Retriever")

# 2. Access attributes
print(my_dog.name)  # Output: Buddy

# 3. Call methods
print(my_dog.bark())      # Output: Buddy says Woof!
print(my_dog.get_info())  # Output: Buddy is a Golden Retriever.