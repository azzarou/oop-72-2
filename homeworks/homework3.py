from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health  # Приватный атрибут
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    def get_health(self):
        return self.__health

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию!")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")

warrior = Warrior("warrior1", 10, 100, 25)
mage = Mage("mage2", 12, 60, 30)
assassin = Assassin("assassin3", 8, 80, 20)

heroes = [warrior, mage, assassin]

for hero in heroes:
    hero.greet()
    hero.attack()
    hero.rest()
