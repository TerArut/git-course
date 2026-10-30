

class Weapon:
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description

    def use(self, target):
        return target.take_damage(self.damage)

    def __str__(self):
        return f"Оружие: {self.name}, урон: {self.damage}, особенность: {self.description}"

class LeviathanAxe(Weapon):
    def __init__(self):
        super().__init__("LeviathanAxe", 150, "Заморозка противника")

    def use(self, target):
        super().use(target)
        target.is_frozen = True

class BladesOfChaos(Weapon):
    def __init__(self):
        super().__init__("BladesOfChaos", 120, "Дополнительный огненный урон")

    def use(self, target):
        super().use(target)
        target.take_damage(30)

