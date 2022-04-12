
class Item:
    def __init__(self, name):
        self.name = name


class Potions(Item):
    # 创建药水类
    def __init__(self, name):
        self.name = name


class Equipments(Item):
    # 创建武器类
    class Weapon:
        def __init__(self, name, damage, weight):
            self.name = name
            self.damage = damage
            self.weight = weight

    # 创建盾牌类
    class Shield:
        def __init__(self, name, armourRating, percentage, weight):
            self.name = name
            self.armourRating = armourRating
            self.percentage = percentage
            self.weight = weight

    # 创建盔甲类
    class Armour:
        def __init__(self, name, armourRating, weight):
            self.name = name
            self.armourRating = armourRating
            self.weight = weight
