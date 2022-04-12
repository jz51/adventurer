from bean.adventurer import Adventurer
from bean.inventory import Inventory
from bean.item import Equipments, Potions


def test():
    w1 = Equipments.Weapon('新手刀', 10, 1)
    s1 = Equipments.Shield('新手盾', 2, 0.5)
    a1 = Equipments.Armour('新手甲', 3, 1)
    potion1 = Potions("healthPotion")
    potion2 = Potions("damagePotion")
    itemsList = [potion1, potion2, w1, s1, a1]

    myInventory = Inventory()
    myInventory.getItem(potion1)
    myInventory.getItem(potion2)
    myInventory.getItem(w1)
    myInventory.getItem(w1)
    myInventory.getItem(w1)
    myInventory.getItem(w1)

    person = Adventurer("无衣", w1, s1, a1, myInventory, 100)
    person.showHero()
    myInventory.getItem(potion2)
    person.showHero()
