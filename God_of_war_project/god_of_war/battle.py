
from character import Kratos, Atreus
from enemies import Draugr, Troll


class Character:
    def __init__(self, name, health, max_health, attack_power, level):
        self.name = name 
        self.max_health = max_health
        self.health = health
        self.attack_power = attack_power
        self.level = level
    
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0 or value > self.max_health:
            raise ValueError
        self._health = value

    def attack(self, target):
        if not self.is_alive():
            raise ValueError("Мёртвый персонаж не может атаковать")
        elif not target.is_alive():
            raise ValueError("Нельзя атаковать мёртвого персонажа")
        else:
            return target.take_damage(self.attack_power)

    
    def take_damage(self, amount):
        if amount > 0:
            if self.health > amount:
                self.health -= amount
            else:
                self.health = 0
            return self.health
        else:
            raise ValueError("Некорректное значение damage amount")

    def heal(self, amount):
        if amount > 0:
            if self.health + amount > self.max_health:
                self.health = self.max_health
            else:
                self.health += amount
            return self.health
        else:
            raise ValueError("Некорректное значение heal amount")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Персонаж: {self.name}, уровень: {self.level}, максимальное здоровье: {self.max_health}, сила атаки: {self.attack_power}, текущее здоровье: {self.health}, жив ли {self.is_alive()}"



def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        character1.attack(character2)
        if character2.is_alive():
            character2.attack(character1)
    if character1.is_alive():
        return character1
    else:
        return character2


# Тест 
draugr1 = Draugr()
draugr2 = Draugr()

winner = battle(draugr1, draugr2)

print(f"В битве одолел {winner.name}")
print(f"Здоровье победителя: {winner.health}")