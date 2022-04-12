import time, os, random


class 人物:
    # 名字，最大血量，当前血量，生存状态，格挡（攻击力？），控制，
    def __init__(self, name, maxHP=100, level=1, stunned=15, blocking=2):
        self.name = name
        self.maxHP = maxHP
        self.hp = maxHP
        self.level = level
        self.minStunned = int(stunned * 0.5)
        self.maxStunned = int(stunned * 1.5)
        self.blocking = blocking
        self.exp = 0
        self.maxEXP = 100
        # self.challenge = 0

    def levelUp(self):
        self.maxHP += 10 + self.level
        self.minStunned += random.randint(2, 8)
        self.maxStunned += random.randint(4, 12)
        self.hp = self.maxHP
        self.blocking += 0.5
        self.exp -= self.maxEXP
        self.maxEXP = int(self.maxEXP * 1.2)
        self.level += 1

    # def viewHero(self):
    #     print('【%s】' % self.name)
    #     print('等级：%d(%d/%d)' % (self.level, self.exp, self.maxEXP))
    #     print('生命值：%d/%d' % (self.hp, self.maxHP))
    #     print('攻击力：%d-%d' % (self.minStunned, self.maxStunned))
    #     print('速度：%.1f' % self.speed)
    #     print('金钱：%d' % self.money)
    #     print('劲敌等级：%d' % self.challenge)
    #     print()
    # viewHero方法：输出冒险者的面板
    def viewHero(self):
        print('英雄名字:', self.name)
        print('最大生命值:', self.maxHP, '\t当前血量:', self.hp)
        print('当前英雄等级:', self.level)
        print(f'控制伤害值范围:[{self.minStunned}，{self.maxStunned}]', '\t格挡值:', self.blocking)

    def stunned(self):
        return random.randint(self.minStunned, self.maxStunned)

    def save(self):
        s = self.name + '\n' + str(self.level) + '\n' + str(self.exp) + '\n' + str(self.maxEXP) + '\n' + str(
            self.hp) + '\n'
        s += str(self.maxHP) + '\n' + str(self.minStunned) + '\n' + str(self.maxStunned) + '\n' + str(self.blocking)
        with open('hero.info', 'w') as f:
            f.write(s)
        print('数据保存完毕!\n')


def 加载勇士():
    global hero
    if os.path.exists('hero.info'):
        try:
            with open('hero.info', 'r') as f:
                d = f.read().split('\n')
            hero = 人物(d[0])
            hero.level = int(d[1])
            hero.exp = int(d[2])
            hero.maxEXP = int(d[3])
            hero.hp = int(d[4])
            hero.maxHP = int(d[5])
            hero.minStunned = int(d[6])
            hero.maxStunned = int(d[7])
            hero.blocking = float(d[8])
            print('欢迎回来，勇士！')
            print()
            return 0
        except Exception as e:
            print('存档读取出错：', e)
            print()

    hero = 人物(input('勇士，取名：'))


def 战斗_伤害事件(A, B):
    global times
    times += 1
    ac = B.stunned()
    A.hp -= ac
    print('<%d>\n【%s】攻击【%s】！\n【%s】受到 %d 点伤害！\n【%s】剩余生命值：%d\n' % (times, B.name, A.name, A.name, ac, A.name, A.hp))
    if A.hp <= 0:
        return 1
    else:
        return 0


def 获取经验系数函数(x):
    if x < 5:
        return -0.198 * x + 1
    if x >= 5:
        return 0.01


def 去打怪(who):
    global times
    try:
        s2 = int(input('你想挑战多少等级的怪物？（>0）'))
    except:
        s2 = 1

    print()
    if s2 > 0:
        os.system('cls')
        print('挑战【%d】级怪物开始！\n' % s2)
        if who.challenge < s2:
            who.challenge = s2

        monster = 人物('怪物' + str(s2) + '号', s2 * 50, s2 * 8, s2 / 5 + 1, s2 * random.randint(0, 20))
        exp = int(s2 * 100 * 获取经验系数函数(who.level - s2))
        if s2 % 10 == 0:
            monster.hp += 40
            monster.minStunned += 6
            monster.maxStunned += 12
            monster.money += s2 // 10 * 200
            exp *= 2
            print('这个怪物异常强大！')

        times = 0
        while monster.hp > 0 and who.hp > 0:
            if monster.speed > who.speed:
                if 战斗_伤害事件(who, monster):
                    break
                time.sleep(0.5)
                if 战斗_伤害事件(monster, who):
                    break
                time.sleep(0.5)
            else:
                if 战斗_伤害事件(monster, who):
                    break
                time.sleep(0.5)
                if 战斗_伤害事件(who, monster):
                    break
                time.sleep(0.5)

        if who.hp > 0:
            if monster.money > 0:
                print('你成功的消灭了怪物，经验和钱包得到了增长！')
            else:
                print('你成功的消灭了怪物，经验得到了增长！')
            who.exp += exp

            ranktmp = 0
            while who.exp >= who.maxEXP:
                who.levelUp()
                ranktmp += 1
            if ranktmp == 1:
                print('【%s】的力量发生了质变！\n' % who.name)
            elif ranktmp > 1 and ranktmp < 100:
                print('【%s】的力量得到了惊人的提升！\n' % who.name)
            elif ranktmp >= 100:
                print('【%s】一定是开了作弊器！\n' % who.name)

            who.money += monster.money
        else:
            print('很遗憾勇士，你被怪物杀死了...游戏结束...')
            print()
            return True
    else:
        print('没有更弱的怪物了，勇士。')
    print()
    return False


def 寻求治疗(who):
    os.system('cls')
    if who.hp < who.maxHP and who.money > 0:
        if who.money >= who.maxHP - who.hp:
            print('在圣光的洗礼下，你恢复如初！')
            who.money -= who.maxHP - who.hp
            who.hp = who.maxHP
        else:
            print('由于你的金钱不够，牧师只治疗了你部分伤势……真是黑暗！')
            who.hp += who.money
            who.money = 0
    else:
        print('你的心灵得到了治愈...')
    print()


加载勇士()
# hero=人物(input('勇士，取名：'))

gameover = False

while gameover == False:
    print('1、去打怪')
    print('2、查看属性')
    print('3、寻求治疗')
    print('4、保存存档')
    print()
    s = input('勇士你现在打算干嘛？（输入序号执行对应操作）')
    print()

    if s == '1':
        gameover = 去打怪(hero)
    elif s == '3':
        寻求治疗(hero)
    elif s == '4':
        os.system('cls')
        hero.save()
    else:
        os.system('cls')
        hero.viewHero()

input('-- Game Over --')
