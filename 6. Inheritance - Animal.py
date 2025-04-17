
class Animal:
    def __init__(self, name: str, colour: str, number_of_feet: int) ->None:
        self.name = name
        self.colour = colour
        self.number_of_feet = number_of_feet

    def speak(self) -> str:
        return f"The {self.name} says Roar"

class Dog(Animal):
    def __init__(self, name: str, colour: str, number_of_feet: int) ->None:
        super().__init__(name, colour, number_of_feet)

    def speak(self) -> str:
        return f"The {self.name} says woof"

class Cat(Animal):
    def __init__(self, name: str, colour: str, number_of_feet: int) -> None:
        super().__init__(name, colour, number_of_feet)


    def speak(self) -> str:
        return f"The {self.name} says meow"

class Snake(Animal):
    def __init__(self, name: str, colour: str, number_of_feet: int) -> None:
        super().__init__(name, colour, number_of_feet)


    def speak(self) -> str:
        return f"The {self.name} says sssss"



dog1 = Dog("labradore", "black", 4)
dog2 = Dog("Saymoed", "blonde", 4)
cat1 = Dog("Sphynx", "brown", 4)
cat2 = Dog("tabby", "orange", 4)
snake = Snake("Python", "Green", 0)