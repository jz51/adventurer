class Inventory:
    def __init__(self):
        self.empty = 6
        self.items = []

    def getItem(self, item):
        if self.empty == 0:
            print("背包放满了，不能再放了，你需要从以下物品中输入序号(-1表示不替换）替换一件物品：")
            self.showBag()
            while 1:
                i = int(input("想要扔掉物品的序号(-1返回上一级表示你不换了）："))
                if i == "-1":  # 上一级
                    break
                else:
                    ack = input("你确认要换这件物品？(Y or N)")
                    if ack == "Y":
                        self.dropItem(i-1)
                    else:
                        print("已取消更换，请重新选择")
                        continue
        self.items.append(item)
        self.empty -= 1

    def dropItem(self, i):
        self.items.pop(i - 1)
        self.empty += 1

    def showBag(self):
        for i in range(len(self.items)):
            item = self.items[i]
            print(f"item{i + 1}:{item.name}")
