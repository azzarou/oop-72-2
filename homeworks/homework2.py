import random

class Hero:

  def __init__(self, name, level, health, strength):
    self.name = name
    self.level = level
    self.health = health
    self.strength = strength

  def greet(self):
    print(f"Привет, я {self.name}, мой уровень {self.level}")

  def attack(self):
    print(f"{self.name} наносит удар!")

  def rest(self):
    print(f"{self.name} отдыхает…")

class Warrior(Hero):

  def __init__(self, name, level, health, strength, stamina):
    super().__init__(name, level, health, strength)
    self.stamina = stamina  # выносливость

  def attack(self):
    print(f"{self.name} (Воин) атакует мечом!")


class Mage(Hero):

  def __init__(self, name, level, health, strength, mana):
    super().__init__(name, level, health, strength)
    self.mana = mana  # мана

  def attack(self):
    print(f"{self.name} (Маг) кастует заклинание!")


class Assassin(Hero):

  def __init__(self, name, level, health, strength, stealth):
    super().__init__(name, level, health, strength)
    self.stealth = stealth  # скрытность

  def attack(self):
    print(f"{self.name} (Ассасин) атакует из-под тишка!")

warrior = Warrior("Артур", 10, 100, 50, 80)
mage = Mage("Мерлин", 10, 80, 30, 100)
assassin = Assassin("Альтаир", 10, 90, 40, 90)

heroes = {"warrior": warrior, "mage": mage, "assassin": assassin}


print("Выберите героя: Warrior / Mage / Assassin")
user_choice = input("Ваш выбор: ").strip().lower()

# Если ввели неправильно, по умолчанию берем Warrior
if user_choice not in heroes:
  user_choice = "warrior"

computer_choice = random.choice(list(heroes.keys()))

print(f"\nВы выбрали: {user_choice}")
print(f"Противник: {computer_choice}\n")

if user_choice == computer_choice:
  print("Ничья!")
elif (
    (user_choice == "warrior" and computer_choice == "assassin")
    or (user_choice == "assassin" and computer_choice == "mage")
    or (user_choice == "mage" and computer_choice == "warrior")
):
  print(f"{user_choice} победил!")
  heroes[user_choice].attack()
else:
  print(f"{computer_choice} победил!")
  heroes[computer_choice].attack()