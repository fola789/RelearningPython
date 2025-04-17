
class Person:
    def __init__(self, name: str, age: int) ->None:
        self.name = name
        self.age = age

    def greet_person(self) ->str:
        return f"Hello, my name is {self.name}"

    def is_adult(self) ->bool:
        if self.age >= 18:
            return True
        else:
            return False

person = Person("Fola", 26)
person2 = Person("Jack", 27)
person3 = Person("James", 14)

print(person.greet_person())
print(person2.greet_person())
print(person3.greet_person())

print(person.is_adult())
print(person2.is_adult())
print(person3.is_adult())
