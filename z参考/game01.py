import random, time, os


# 创建冒险者类
# 构造函数：用于记录冒险者名称并设置各属性的技能，面板里面有
# 名字(name),最大血量(maxHP), 当前血量(hp), 活着(alive)的情况下的状态，格挡(blocking)和控制（眩晕敌人stunned）
class Adventurer():
    def __init__(self, name, maxHP, hp, alive, stunned, blocking):
        self.name = name
        print('冒险者' + self.name + '诞生了，开启你的战斗吧！')
        self.maxHP = random.randint(4500, 5000)  # 冒险者的最大血量
        self.hp = 5000  # 冒险者的血量
        self.alive = 1  # 冒险者的当前状态为1级
        self.stunned = 15  # 冒险者的控制晕眩值（相当于攻击力）
        self.blocking = 20  # 冒险者的格挡值（相当于防御值）

    # setability方法：
    # 用于修改冒险者面板，实现冒险者成长和变化，例如装装备了、受伤了、吃药了等等。
    def setability(self, a, d, hp):
        self.stunned += a
        self.blocking += d

    # viewHero方法：输出冒险者的面板
    def viewHero(self):
        print('当前英雄等级:', self.alive)
        print('最大生命值:', self.maxHP, '\t当前血量:', self.hp)
        print('控制晕眩值:', self.stunned, '\t格挡值:', self.blocking)


class Items:  # 这是物品的父类
    Itename = '物品'

    def __init__(self, name):
        self.Itename = name


# class Potions(Items):
# def healthPotion(self, )


class Equipments(Items):  # 这是装备类

    # Weapons：设置武器中有名字（name），伤害（damage），重量（weight）。
    def Weapons(self, damage, weight):
        self.damage = damage
        self.weight = weight
        return None

    # 武器有以下10种可以选择
    weapons1 = Weapons("Redsword", '15', 1)
    weapons2 = Weapons('Orangesword', '20', 1.5)
    weapons3 = Weapons('Yellowsword', '30', 2)
    weapons4 = Weapons('Greensword', '40', 2.5)
    weapons5 = Weapons('Cyansword', '50', 3)
    weapons6 = Weapons('Bluesword', '60', 3.5)
    weapons7 = Weapons('Purplesword', '70', 4)
    weapons8 = Weapons('Lightsword', '80', 4.5)
    weapons9 = Weapons('Darksword', '90', 5)
    weapons10 = Weapons('Excalibur', '100', 1)

    # Shields有名字， 防御值（armourRating），重量和眩晕对手的几率（percentage）
    def Shields(self, armourRating, weight, percentage):
        self.armourRating = armourRating
        self.weight = weight
        self.percentage = percentage

    # 盾牌有以下10中可以选择
    shields1 = Shields('Redshield', 10, 1.5, 0.1)
    shields2 = Shields('Orangeshield', 15, 2, 2)
    shields3 = Shields('Yellowshield', 20, 2.5, 0.2)
    shields4 = Shields('Greenshield', 30, 3, 0.25, )
    shields5 = Shields('Cyanshield', 40, 3.5, 0.3)
    shields6 = Shields('Blueshield', 50, 4, 0.35)
    shields7 = Shields('Purpleshield', 60, 4.5, 0.4)
    shields8 = Shields('Lightshield', 70, 5, 0.45)
    shields9 = Shields('Darkshield', 80, 5.5, 0.5)
    shields10 = Shields('Mirrorshield', 90, 6, 0.6)

    def Armour(self, armourRating, weight):
        self.armourRating = armourRating
        self.weigh = weight

    armour1 = Armour('Redarmour', 10, 2)
    armour2 = Armour('Orangearmour', 15, 2.5)
    armour3 = Armour('Yellowarmour', 20, 3)
    armour4 = Armour('Greenarmour', 30, 3.5)
    armour5 = Armour('Cyanarmour', 40, 4)
    armour6 = Armour('Bluearmour', 50, 4.5)
    armour7 = Armour('Purplearmour', 60, 5)
    armour8 = Armour('Lightarmour', 70, 5.5)
    armour9 = Armour('Darkarmour', 80, 6)
    armour10 = Armour('Goldenarmour', 100, 8)


def setEstate(self, type):
    # setEstate方法：改变装备的装备状态。装了的卸，没装的装。
    if self.Estate == '未装备':
        self.Estate == '已装备'
        type.setability(self.addstunned, self.addblocking, 0, 0)
    elif self.Estate == '已装备':
        self.Estate == '未装备'
        type.setability(-1 * self.addstunned, 1 * self.addblocking, 0, 0)


def setEquipment(self):
    self.Etype = self.Etypes[self.typed]
    self.addstunned = self.pinji * random.randint(30, 40)
    self.addblocking = self.pinji * random.randint(25, 35)
    if self.Etype == '武器':
        self.addblocking == 0
    elif self.Etype == '防御':
        self.addstunned == 0


Adventurer()
