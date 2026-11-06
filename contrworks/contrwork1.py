class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return self.__password == password

    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Класс: {type(self.hero).__name__}, Баланс: {self._balance} SOM"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl

mage1 = MageHero("Merlin", 50, 100, 150)
mage2 = MageHero("Gandalf", 50, 90, 200)
warrior = WarriorHero("Conan", 50, 200)

print(mage1.action())
print(warrior.action())

acc1 = BankAccount(hero=mage1, balance=5000, password="123", bank_name="Simba")
acc2 = BankAccount(hero=mage2, balance=3000, password="456", bank_name="Simba")
acc3 = BankAccount(hero=warrior, balance=4000, password="789", bank_name="Simba")

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("Mage1 == Mage2 ", acc1 == acc2)
print("Mage1 == Warrior ", acc1 == acc3)
