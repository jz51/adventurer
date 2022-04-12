# from actions import action, enemyAction
import random

import actions
from bean.adventurer import Adventurer
from bean.item import Equipments, Potions
from bean.inventory import Inventory
from bean.items import getItemsList


def initAdventurer(name):
    w1 = Equipments.Weapon('新手刀', 10, 1)
    s1 = Equipments.Shield('新手盾', 2, 0.3, 1)
    a1 = Equipments.Armour('新手甲', 3, 1)
    potion1 = Potions("healthPotion")
    potion2 = Potions("damagePotion")
    myInventory = Inventory()
    myInventory.getItem(potion1)
    myInventory.getItem(potion2)
    adventurer = Adventurer(name, w1, s1, a1, myInventory, 200)
    return adventurer


def initEnemy(enemyNum):
    # 后续可以考虑随机怪兽的装备和初始血量
    enemyName = f"怪物{enemyNum}号"
    w1 = Equipments.Weapon('新手刀', 10, 1)
    s1 = Equipments.Shield('新手盾', 2, 0.3, 1)
    a1 = Equipments.Armour('新手甲', 3, 1)
    enemy = Adventurer(enemyName, w1, s1, a1, Inventory(), 50)
    return enemy


def randomEnemy(enemyNum):
    itemsList = getItemsList()
    enemyName = f"怪物{enemyNum}号"
    wNum = random.randint(0, 5)
    sNum = random.randint(6, 11)
    aNum = random.randint(12, 17)
    randomHP = random.randint(40 + 6 * enemyNum, 80 + 6 * enemyNum)  # 这里用enemyNum系数加成
    enemy = Adventurer(enemyName, itemsList[wNum], itemsList[sNum], itemsList[aNum], Inventory(), randomHP)
    return enemy


def settleRound(adv, enemy, enemySub, advAdd, advSub, enemyAdd):
    # 结算勇士
    if enemy.blocking == 'false':  # 怪兽不格挡，才会攻击，才需要统计血量
        if adv.blocking == 'true':
            if advSub > advAdd:  # 格挡且对面攻击护甲之后掉的血比盾牌挡的多
                adv.hp = adv.hp - advSub + advAdd
            elif advSub != 0:
                adv.hp -= 1
        else:
            if advSub > 0:
                adv.hp = adv.hp - advSub
            elif advSub != 0:  # 对面攻击没我护甲高，掉1 且怪兽不是格挡
                adv.hp -= 1
    else:  # 怪兽格挡，不用管勇士血量了
        pass

    # 结算怪物
    if adv.blocking == 'false':  # 勇士不格挡，才会攻击，才更新怪兽血量
        if enemy.blocking == 'true':
            if enemySub > enemyAdd:  # 对面攻击护甲之后掉的血比盾牌挡的多
                enemy.hp = enemy.hp - enemySub + enemyAdd
            elif enemySub != 0:  # 对面攻击护甲之后掉的血比盾牌挡的少
                enemy.hp -= 1
        else:
            if enemySub > 0:
                enemy.hp = enemy.hp - enemySub
            elif enemySub != 0:  # 我攻击没对面护甲高，掉1
                enemy.hp -= 1
    else:  # 我格挡了，怪兽无所谓
        pass

    # 刷新状态
    adv.showStatus()
    enemy.showStatus()
    adv.blocking = 'false'
    enemy.blocking = 'false'
    if adv.hp <= 0:
        adv.alive = 'false'
    if enemy.hp <= 0:
        enemy.alive = 'false'


def battle(adv):
    global win
    win = 0
    # 如果勇士活着，则创建随机敌人
    print("你遇到了一只怪物，敌人信息如下：")
    if enemyNum < 3:
        enemy = initEnemy(enemyNum)
    else:
        enemy = randomEnemy(enemyNum)
    print(enemy.showHero())
    if adv.getWeight() <= enemy.getWeight():  # 谁轻谁先手，一样你先手
        while adv.isAlive() == "true" and enemy.isAlive() == "true":  # 都活着就继续干
            enemySub, advAdd, advSub, enemyAdd = 0, 0, 0, 0
            enemySub, advAdd = actions.action(adv, enemy)  # 冒险者打怪兽
            if enemySub == -99 and advAdd == -99:
                return
            advSub, enemyAdd = actions.enemyAction(enemy, adv)  # 怪兽打冒险者
            settleRound(adv, enemy, enemySub, advAdd, advSub, enemyAdd)  # 结算这一回合
    else:
        while adv.isAlive() == "true" and enemy.isAlive() == "true":  # 都活着就继续干
            enemySub, advAdd, advSub, enemyAdd = 0, 0, 0, 0
            advSub, enemyAdd = actions.enemyAction(enemy, adv)  # 怪兽打冒险者
            enemySub, advAdd = actions.action(adv, enemy)  # 冒险者打怪兽
            if enemySub == -99 and advAdd == -99:
                return
            settleRound(adv, enemy, enemySub, advAdd, advSub, enemyAdd)  # 结算这一回合
    if enemy.alive == 'false':
        print("===========================牛批，恭喜你战胜了怪兽===================================================")
        win = 1


def inventoryManagement(adv, itemsList):
    global enemyNum
    print("===========================即将迎接下一个怪兽，请做好准备===================================================")
    empty0 = adv.inventory.empty
    while 1:
        print("你有如下选择：")
        print("1.挑选胜利奖品pick up items")
        print("2.丢弃物品栏物品drop held items")
        print("3.装备物品栏物品equip held items")
        print("4.继续战斗fight next enemy")
        choice = input("请输入你的胜利选择(-1表示退出)：")
        # switch在python3.10的版本之前只能通过字典实现，此处不努力了。
        if choice == "1":
            if win == 1:
                if empty0 - adv.inventory.empty < 3:
                    actions.pickUpItem(adv, itemsList)
                else:
                    print("你已经挑选了三个奖品了，请不要利用漏洞多选哦~")
            else:
                print("\n----------------你击败了怪兽吗就想领奖励？逃跑可是没有战利品的------------------\n")
        elif choice == "2":
            actions.dropItem(adv)
        elif choice == "3":
            actions.equipItem(adv)
        elif choice == "4":
            enemyNum += 1
            battle(adv)
        elif choice == '-1':
            break
        else:
            print("输入指令无效，请重新输入：")
            continue


global enemyNum, win
global itemsList
if __name__ == '__main__':
    # test()
    # 初始化一些参数
    enemyNum = 0
    win = 0
    itemsList = getItemsList()

    # 创建勇士
    name = input("欢迎来到冒险岛，请为勇士创建一个名字：")
    adventurer = initAdventurer(name)
    adventurer.showHero()

    print()
    print("欢迎来到新世界，努力打倒敌人变得更强吧，勇士，请踏上你的征程！")
    print("*****************************************************************")
    print()
    while adventurer.alive == "true":
        enemyNum += 1
        battle(adventurer)
        inventoryManagement(adventurer, itemsList)
