'''
@author: ldc

'''
'''
提款机：
类名：ATM
属性：
行为：开户,查询,取款,存储,转账,销户,挂失,解锁,改密,退出
'''
from check import Check
from card import Card
from readAppendCard import ReadCard,AppendCard
import random
import time


class ATM(object):
    # 开户
    def __init__(self):
        self.check = Check()
        self.readCard = ReadCard()
        self.appendCard = AppendCard()
        self.cards = self.readCard.read()
    def newAccount(self):
        # 输入身份证号和手机号
        pnum = self.check.phoneNumInput()
        iden = self.check.identifyInput()
        print("正在执行开户程序，请稍候...")

        while True:
            # 生成6位的随机卡号
            # cardId = ['1','2','3','4','5','6','7','8','9','0']
            # random.shuffle(cardId)
            # cardId = ''.join(cardId[:6])

            cardId = str(random.randrange(100000, 10000000))

            if cardId[0] == '0':
                continue
            if self.check.isCardIdExist(self.cards,cardId) == False:
                break
            else:
                continue

        # 初始化卡号密码，卡里的钱，卡的锁定状态
        card = Card(cardId, '888888', 0, iden, pnum , 'False')

        self.appendCard.append(card)
        print("开户成功，您的卡号为%s，密码为%s,卡余额为%d。"%(cardId,'888888',0))
        print("请牢记密码，不要把密码泄露给他人。")
        # 更新卡号列表
        self.cards = self.readCard.read()
        return True

    # 查询
    def checkMoney(self):
        card = self.check.isCardExist(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        print("您的余额为%d元！" % card.cardMoney)
        time.sleep(1)
        return card.cardMoney
    # 存储
    def saveMoney(self):
        card = self.check.isCardExist(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        mon = int(input("请输入您要存的钱："))
        index = self.cards.index(card)
        self.cards[index].cardMoney += mon
        self.writeCard()

        print("存款成功！您卡上的余额为%d元!"%self.cards[index].cardMoney)
        time.sleep(1)
        pass

    # 取款
    def getMoney(self):
        card = self.check.isCardExist(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        mon = int(input("请输入您要取的钱："))
        index = self.cards.index(card)
        if mon > self.cards[index].cardMoney:
            print("余额不足，您当前余额为%d元!"%self.cards[index].cardMoney)
            time.sleep(1)
            return
        self.cards[index].cardMoney -= mon
        self.writeCard()

        print("取款成功！你卡上的余额为%d元!"%self.cards[index].cardMoney)
        time.sleep(1)
        pass
    # 转账
    def transferMoney(self):
        card = self.check.isCardExist(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        while True:
            cardId = input("请输入对方的账号：")
            cardOther = self.check.isCardIdExist(self.cards,cardId)
            if cardOther == False:
                print("账号不存在")
                if self.check.isSure("继续转账"):
                    continue
                else:
                    time.sleep(1)
                    return
            else:
                break
        index = self.cards.index(card)
        while True:
            mon = int(input("您当前的余额为%d,请输入要转账的钱："%self.cards[index].cardMoney))

            if mon > self.cards[index].cardMoney:
                print("余额不足，您当前余额为%d元!" % self.cards[index].cardMoney)
                if self.check.isSure("继续转账"):
                    continue
                else:
                    time.sleep(1)
                    return
            else:
                self.cards[index].cardMoney -= mon
                break
        indexOther = self.cards.index(cardOther)
        self.cards[indexOther].cardMoney += mon
        self.writeCard()

        print("转账成功！你卡上的余额为%d元!" % self.cards[index].cardMoney)
        time.sleep(1)
        pass
    # 销户
    def closeAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        if card:
            self.cards.remove(card)
            self.writeCard()

            print("销户成功！")
            time.sleep(1)
        pass
    # 挂失
    def lockAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        if card:
            index = self.cards.index(card)
            self.cards[index].cardLock = "True"
            self.writeCard()

            print("挂失成功！")
            time.sleep(1)
        pass
    # 解锁
    def unlockAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        index = self.cards.index(card)
        self.cards[index].cardLock = "False"
        self.writeCard()

        print("解锁成功！")
        time.sleep(1)
        pass
    # 改密
    def changePassword(self):
        card = self.check.isCardInfoSure(self.cards)
        if self.check.isCardLock(self.cards, card.cardId):
            return
        # 输入旧密码
        while True:
            password = input("请输入旧密码")
            if self.check.isCardPasswordSure(password,card.cardPassword):
                break
            else:
                print("卡号密码输入错误！")
                if self.check.isSure("修改密码"):
                    continue
                else:
                    return

        newpassword = input("请输入新密码")
        index = self.cards.index(card)
        self.cards[index].cardPassword = newpassword
        self.writeCard()

        print("改密成功！")
        time.sleep(1)

        pass
    # 写入文件
    def writeCard(self):
        self.appendCard.append('', w='w')
        for card in self.cards:
            self.appendCard.append(card)
    # 退出
    def exit(self):
        if self.check.isSure("退出"):
            return True
        else:
            return False
        pass

# 测试
def main():
    atm = ATM()
    print(atm.newAccount())

if __name__ == '__main__':
    main()


