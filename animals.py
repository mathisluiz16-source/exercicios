class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "..."

class dog(animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        return "Woof!"

class cat(animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def make_sound(self):
        return "Meow!"

animals = [dog("Buddy"), cat("Whiskers")]
for a in animals:
    print(a.make_sound())