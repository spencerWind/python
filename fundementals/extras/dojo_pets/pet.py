# PET CLASS

class Pet:
    def __init__(self, name, tricks) -> None:
            self.name = name
            self.tricks = tricks
            self.health = 100
            self.energy = 100

    def sleep(self):
            self.energy += 25
            return self

    def eat(self):
            self.energy += 5
            self.health += 10
            return self

    def play(self):
            self.health += 5
            return self

    def noise(self):
            print('I am not a defined pet, so i dont have a noise!')
            return self
    
class Dog(Pet):
    def __init__(self, name, tricks) -> None:
        super().__init__(name, tricks)
        self.pet_type = 'Dog'
        self.pet_sound = 'Bark'

class Cat(Pet):
    def __init__(self, name, tricks) -> None:
        super().__init__(name, tricks)
        self.pet_type = 'Cat'
        self.pet_sound = 'Meow'