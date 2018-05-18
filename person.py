'''
@author: ldc

'''
'''
人
类名：Person
属性：姓名  身份证号   电话号  卡
行为：开户   查询   取款   存储   【转账   改密
   销户  退出】

'''

class Person(object):

    def __init__(self,name,identity,phoneNum,card=None):
        self.name = name
        self.identity = identity
        self.phoneNum = phoneNum
        self.card = card

    def newAccount(self,atm):
        atm.newAccount()

    def checkMoney(self, atm):
        atm.checkMoney()

    def saveMoney(self, atm):
        atm.saveMoney()

    def getMoney(self, atm):
        atm.getMoney()

    def transferMoney(self, atm):
        atm.transferMoney()

    def closeAccount(self, atm):
        atm.closeAccount()

    def lockAccount(self, atm):
        atm.lockAccount()

    def unlockAccount(self, atm):
        atm.unlockAccount()

    def changePassword(self, atm):
        atm.changePassword()

    def exit(self, atm):
        atm.exit()
