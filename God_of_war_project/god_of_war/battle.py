
from .character import Kratos, Atreus
from .enemies import Draugr, Troll
from .weapons import LeviathanAxe


def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        character1.attack(character2)
        if character2.is_alive():
            if character2.is_frozen:
                character2.is_frozen = False
            else:
                character2.attack(character1)
    if character1.is_alive():
        return character1
    else:
        return character2


# Тест 
kratos1 = Kratos(2); # kratos1.equip_weapon(LeviathanAxe())
graugr1 = Draugr(3)

winner = battle(kratos1, graugr1)

print(f"В битве одолел {winner.name}")
print(f"Здоровье победителя: {winner.health}")