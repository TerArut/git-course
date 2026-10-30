# Закрепление материала
## Гиты - 1

class Character:
    def __init__(self, name, health, max_health, attack_power, level):
        self.name = name 
        self.max_health = max_health
        self.health = health
        self.attack_power = attack_power
        self.level = level
        self.weapon = None
        self.is_frozen = False
        self.inventory = []

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0 or value > self.max_health:
            raise ValueError
        self._health = value

    def equip_weapon(self, weapon):
        if weapon not in self.inventory:
            raise ValueError("Этого оружия нет в инвентаре")

        self.weapon = weapon
        self.inventory.remove(weapon)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def attack(self, target):
        if not self.is_alive():
            raise ValueError("Мёртвый персонаж не может атаковать")
        elif not target.is_alive():
            raise ValueError("Нельзя атаковать мёртвого персонажа")
        elif self.weapon != None:
            print(f"{self.name} атакует {target.name}!")
            return self.weapon.use(target)
        else:
            print(f"{self.name} наносит {self.attack_power} урона!")
            print(f"{self.name} атакует {target.name}!")
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



class Kratos(Character):
    def __init__(self, level):
        super().__init__("Kratos", 500, 500, 100, level)
    

class Atreus(Character):
    def __init__(self, level):
        super().__init__("Atreus", 250, 250, 50, level)


