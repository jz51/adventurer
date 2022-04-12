class Adventurer:
    # 名字name，最大血量maxHP，当前血量hp，生存状态alive，格挡blocking，控制stunned，
    def __init__(self, name, weapon, shield, armour, inventory, maxHP=100):
        self.name = name
        self.maxHP = maxHP
        self.hp = maxHP
        self.alive = 'true'
        self.stunned = 'false'
        self.blocking = 'false'

        # 初始化装备
        self.weapon = weapon  # 初始化武器设置
        self.shield = shield
        self.armour = armour
        # 初始化物品栏
        self.inventory = inventory

    # showHero：输出冒险者的面板
    def showHero(self):
        print('名字:', self.name)
        self.showStatus()
        self.showEquipment()
        self.showInventory()

    def isAlive(self):
        if self.hp <= 0:
            self.alive = 'false'
            return "false"
        else:
            self.alive = 'true'
            return "true"

    def showStatus(self):
        print('状态:')
        print('最大生命值:', self.maxHP, '\t当前血量:', self.hp, '\talive:', self.alive)
        print('stunned:', self.stunned, '\tblocking:', self.blocking)

    def showEquipment(self):
        print('装备:')
        print(f"weapon:\tname={self.weapon.name};\tdamage={self.weapon.damage};\t\tweight={self.weapon.weight};")
        print(
            f"shield:\tname={self.shield.name};\tarmourRating={self.shield.armourRating};\tweight={self.shield.weight};\tpercentage={self.shield.percentage}")
        print(f"armour:\tname={self.armour.name};\tarmourRating={self.armour.armourRating};\tweight={self.armour.weight}")

    def showInventory(self):
        print('物品栏:')
        num = len(self.inventory.items)
        if num == 0:
            print("空的。")
        else:
            for i in range(num):
                item = self.inventory.items[i]
                print(f"item{i + 1}:\t{item.name}")

    def getWeight(self):
        return self.weapon.weight+self.armour.weight+self.shield.weight


