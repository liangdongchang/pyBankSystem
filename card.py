'''
@author: ldc

'''

'''
卡:
类名:Card
属性：卡号【6位随机】   密码   余额  绑定的身份证号 手机号
'''
class Card(object):
    def __init__(self, cardId, cardPassword, cardMoney,identityId,phoneNum,cardLock=''):
        self.cardId = cardId
        self.cardPassword = cardPassword
        self.cardMoney = cardMoney
        self.identityId = identityId
        self.phoneNum = phoneNum
        self.cardLock = cardLock

