import random
import re

from game0 import initAdventurer, randomEnemy, battle


def attack(attacker=initAdventurer("无衣"), victim=randomEnemy(0)):
    attacker.blocking = 'false'
    eSub = attacker.weapon.damage - victim.armour.armourRating
    return eSub


def defend(attacker=initAdventurer("无衣"), victim=randomEnemy(0)):
    attacker.blocking = "true"  # 设置为格挡，直到冒险者选择攻击或者使用物品或者冒险者受到伤害。
    aAdd = attacker.shield.armourRating
    # 设置一个自由值（random number）在0到1之间，如果这个值等于盾牌眩晕对手的几率（percentage），设置对手的被控制状态（stunned）为true，对手必须跳过这一回合。
    safePer = random.random()  # 产生随机浮点数，小于等于概率就是晕了
    if safePer <= attacker.shield.percentage:
        print("============格挡成功并眩晕了=========")
        victim.stunned = "true"
    else:
        print("==============格挡失败，不眩晕===========")
        victim.stunned = "false"
    return aAdd


def usePotion(adv=initAdventurer("无衣"), enemy=randomEnemy(0)):
    adv.blocking = 'false'
    adv.showInventory()
    while 1:
        dex = input("请输入序号选择你要使用的物品(没有药的话用-1后退），战斗状态只能用药品，希望你不要不识好歹:")
        if dex == "-1":  # 没有药就让他重新选择干嘛，不然就死循环了
            action(adv, enemy)
            break
        elif len(adv.inventory.items) < int(dex):
            print("序号超出背包物品范围了，物品不存在，请重新选择!")
            continue
        else:
            dex = int(dex)
            item = adv.inventory.items[dex - 1]
            if "Potion" in item.name:  # 如果是药品，就用
                adv.inventory.items.pop(dex - 1)  # 把物品从背包取出来
                if item.name == "healthPotion":
                    adv.hp += 200
                    if adv.hp > adv.maxHP:
                        adv.hp = adv.maxHP
                if item.name == "damagePotion":
                    enemy.hp -= 50
                    if enemy.hp <= 0:
                        enemy.alive = "false"
                break
            else:
                print("重新选！只能使用药品")


def runAway():
    print("不要气馁，再试试能不能抽到较弱的怪兽，实在不行就自杀吧。")
    # battle(adv)


def action(adv, enemy):
    eSub, aAdd = 0, 0
    if adv.stunned == 'true':
        print("你被对面用盾牌格挡眩晕了，将跳过这回合")
        adv.stunned = 'false'
        return eSub, aAdd

    print("你有如下选择：")
    print("1.攻击attack")
    print("2.格挡block")
    print("3.使用物品use an item")
    print("4.逃跑run away")

    while 1:
        choice = input("请输入你的选择：")
        # switch在python3.10的版本之前只能通过字典实现，此处不努力了。
        if choice == "1":
            eSub = attack(adv, enemy)
        elif choice == "2":
            aAdd = defend(adv, enemy)
        elif choice == "3":
            usePotion(adv, enemy)
        elif choice == "4":
            runAway()
            return -99, -99
        else:
            print("输入指令无效，请重新输入：")
            continue
        break

    return eSub, aAdd


def enemyAction(enemy, adv):
    aSub, eAdd = 0, 0
    if enemy.stunned == 'true':
        print("怪兽被你用盾牌格挡眩晕了，将跳过这回合")
        enemy.stunned = 'false'
        return aSub, eAdd
    ran = random.randint(1, 2)
    if ran == 1:
        print("=======怪兽选择进攻======")
        aSub = attack(enemy, adv)
    if ran == 2:
        print("=======怪兽选择格挡=====")
        eAdd = defend(enemy, adv)

    return aSub, eAdd


def pickUpItem(adv, itemsList):
    wNum = random.randint(0, 5)
    sNum = random.randint(6, 11)
    aNum = random.randint(12, 17)
    potionNum = random.randint(18, 19)
    winList = [itemsList[wNum], itemsList[sNum], itemsList[aNum], itemsList[potionNum]]
    # print(winList)
    for i in range(len(winList)):
        item = winList[i]
        print(f"item{i + 1}:{item.name}")
    for i in range(1, 4):
        dex = input("请输入序号选择你要的物品(-1返回上一级表示你不要物品，将直接开始战斗）:")
        # =======================有个bug，如果这里选1个2个出去了，其实就可以无限刷装备。=============
        # 已修复：在pickUp的入口处加了个判断
        if dex == "-1":  # 上一级
            break
        elif len(re.findall("\d", dex)) == 0:  # 如果不是数字
            print("输入指令无效，请重新输入:")
            continue
        else:
            ack = input("你确认要这件物品？(Y or N):")
            if ack == "Y":
                dex = int(dex)
                item = winList[dex - 1]
                adv.inventory.getItem(item)  # 把物品从背包取出来
                # adv.inventory.showBag()
            else:
                print("已取消捡起，请重新选择")
                continue


def dropItem(adv=initAdventurer(" ")):
    adv.showInventory()
    while 1:
        dex = input("请输入序号选择你要丢弃的物品(-1返回上一级）:")
        if dex == "-1":  # 上一级
            break
        else:
            ack = input("你确认要丢这件物品？(Y or N)")
            if ack == "Y":
                dex = int(dex)
                adv.inventory.items.pop(dex - 1)  # 把物品从背包取出来
            else:
                print("已取消丢弃，请重新选择")
                continue


def equipItem(adv):
    adv.showInventory()
    while 1:
        dex = input("请输入序号选择你要装备的物品(没有装备的话用-1后退），不能用药品，希望你不要不识好歹:")
        if dex == "-1":  # 退出换装，不然就死循环了
            print("退出换装")
            break
        else:
            dex = int(dex)
            item = adv.inventory.items[dex - 1]
            if "Potion" in item.name:  # 如果是药品
                print("重新选！只能使用装备")
            elif "sword" in item.name:  # 如果是武器
                # adv.inventory.items.pop(dex - 1)  # 把物品从背包取出来
                adv.inventory.dropItem(dex-1)  # 把物品从背包取出来
                adv.inventory.getItem(adv.weapon)  # 把装备放进背包
                adv.weapon = item  # 把取出的装备换上
                adv.showInventory()
                continue
            elif "shield" in item.name:  # 如果是盾
                # adv.inventory.items.pop(dex - 1)  # 把物品从背包取出来
                adv.inventory.dropItem(dex-1)  # 把物品从背包取出来
                adv.inventory.getItem(adv.weapon)  # 把装备放进背包
                adv.shield = item  # 把取出的装备换上
                adv.showInventory()
                continue
            elif "armour" in item.name:  # 如果是护甲
                # adv.inventory.items.pop(dex - 1)  # 把物品从背包取出来
                adv.inventory.dropItem(dex-1)  # 把物品从背包取出来
                adv.inventory.getItem(adv.weapon)  # 把装备放进背包
                adv.armour = item  # 把取出的装备换上
                adv.showInventory()
                continue
            else:
                print("这是bug，可能是我给装备改名字了")
