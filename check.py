'''
@author: ldc

'''
'''
验证类：
用户名、密码、卡号、身份证、手机号验证
输入确认
'''

class Check(object):
    def __init__(self):
       pass
    #用户验证
    def userName(self,admin,password):
        self.admin = admin
        self.password = password
        adminFlag = False
        admin = input("请输入用户名：")
        while True:
            # 如果用户名输对，但密码输错，那么重新输入时只需输入密码验证即可
            if adminFlag:
                admin = input("请输入用户名：")
            password = input("请输入密码：")
            if admin != self.admin:
                print("输入的用户名不对，请重新输入！")
                adminFlag = True
                continue
            elif password != self.password:
                print("输入的密码不对，请重新输入！")
                adminFlag = False
                continue
            else:
                return

    #是否确认某操作
    def isSure(self,operate):
        while True:
            res = input("是否确认%s?【yes/no】"%operate)
            if res not in ['yes','no']:
                print("输入有误，请重新输入！")
                continue
            elif res == 'yes':
                return True
            else:
                return False

    # 手机号验证
    def isPhoneNum(self,phonenum):
        if phonenum[0] != '1' :
            print("输入的手机号开头不为1，请重新输入！")
            return False
        elif len(phonenum) != 11 :
            print("输入的手机号长度不对【11位】，请重新输入！")
            return False
        elif not phonenum.isdigit():
            print("输入的手机号必须全部是数字，请重新输入！")
            return False
        else:
            return True

    def phoneNumInput(self):
        while True:
            pnum = input("请输入您的手机号：")
            if self.isPhoneNum(pnum):
                return pnum

    def identifyInput(self):
        iden = input("请输入您的身份证号：")
        return iden
    # 卡号和密码是否正确
    def isCardExist(self,cards):
        cardId = input("请输入账号：")
        password = input("请输入密码：")

        while True:
            for card in cards:
                if cardId == card.cardId:
                    if password == card.cardPassword:
                        return card
                    else:
                        password = input("密码有误，请重新输入密码：")
                        break
            else:
                cardId = input("账号不存在，请重新输入账号：")
                password = input("请输入密码：")

    # 卡号是否存在
    def isCardIdExist(self,cards,cardId):
        for card in cards:
            if cardId == card.cardId:
                return card
        else:
            return False

    # 卡号密码是否正确
    def isCardPasswordSure(self, newassword,oldpassword):

        if newassword == oldpassword:
            return True
        else:
           return False

    def isCardInfoSure(self,cards):
        # 卡号和密码是否正确
        card = self.isCardExist(cards)
        idenId = self.identifyInput()
        pnum = self.phoneNumInput()
        while True:
            if card.identityId == idenId:
                if card.phoneNum != pnum:
                    print("预留手机号输入不对。")
                    if self.isSure("继续注销卡号%s"%card.cardId):
                        pnum = self.phoneNumInput()
                        continue
                    else:
                        return False
                else:
                    return card
            else:
                print("身份证号输入不对。")
                if self.isSure("继续注销卡号%s" % card.cardId):
                    idenId = self.identifyInput()
                    continue
                else:
                    return False
    # 卡号是否锁定
    def isCardLock(self,cards,cardId):
        card = self.isCardIdExist(cards,cardId)
        # print(card.cardLock)
        if card != False:
            if card.cardLock == "False":
                return False
            else:
                print("此卡已挂失！")
                return True
        else:
            return "卡号不存在"


# 测试
def main():
    check = Check()
    # print(check.isSure('注销'))
    print(check.phoneNumInput())


if __name__ == '__main__':
    main()
