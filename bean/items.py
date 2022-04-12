from bean.item import Equipments, Potions


def getItemsList():
    w1 = Equipments.Weapon('Redsword', 15, 1)
    s1 = Equipments.Shield('Redshield', 10, 1.5, 0.1)
    a1 = Equipments.Armour('Redarmour', 10, 2)

    w2 = Equipments.Weapon('Orangesword', 15, 1)
    s2 = Equipments.Shield('Orangeshield', 15, 2, 0.15)
    a2 = Equipments.Armour('Orangearmour', 15, 2.5)

    w3 = Equipments.Weapon('Yellowsword', 20, 1.5)
    s3 = Equipments.Shield('Yellowshield', 20, 2.5, 0.2)
    a3 = Equipments.Armour('Yellowarmour', 10, 2)

    w4 = Equipments.Weapon('Greensword', 40, 2.5)
    s4 = Equipments.Shield('Greenshield', 30, 3, 0.25)
    a4 = Equipments.Armour('Greenarmour', 30, 3.5)

    w5 = Equipments.Weapon('Cyansword', 50, 3)
    s5 = Equipments.Shield('Cyanshield', 40, 3.5, 0.3)
    a5 = Equipments.Armour('Cyanarmour', 40, 4)

    w6 = Equipments.Weapon('Bluesword', 60, 3.5)
    s6 = Equipments.Shield('Blueshield', 50, 4, 0.35)
    a6 = Equipments.Armour('Bluearmour', 50, 4.5)

    potion1 = Potions("healthPotion")
    potion2 = Potions("damagePotion")
    itemsList = [w1, w2, w3, w4, w5, w6, s1, s2, s3, s4, s5, s6, a1, a2, a3, a4, a5, a6, potion1, potion2]

    return itemsList

