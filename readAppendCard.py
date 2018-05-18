'''
@author: ldc

'''
from card import Card
import json

# 读
class ReadCard(Card):
    def __init__(self, cardId='', cardPassword='', cardMoney=0, identityId='', phoneNum='', cardLock=''):
        Card.__init__(self, cardId, cardPassword, cardMoney, identityId, phoneNum, cardLock)

    def dict2Card(self, d):
        return self.__class__(d["cardId"], d["cardPassword"], d["cardMoney"],d["identityId"],d["phoneNum"], d["cardLock"])

    def read(self):
        # card对象转为字典
        with open("cardinfo.txt","r",encoding="utf-8") as fr:
            cards = []
            for re in fr.readlines():
                cards.append(self.dict2Card(eval(re)))
        return cards

# 写
class AppendCard(Card):
    def __init__(self):
        Card.__init__(self, cardId = '', cardPassword = '', cardMoney = 0, identityId = '', phoneNum = '', cardLock='')

    def card2Dict(self,card):
        return {"cardId": card.cardId, "cardPassword": card.cardPassword,
                "cardMoney": card.cardMoney, "identityId": card.identityId,
                "phoneNum": card.phoneNum, "cardLock": card.cardLock
                }

    def append(self,card,w= 'a'):
        # 清除
        if w == 'w':
            with open("cardinfo.txt", "w", encoding="utf-8") as fa:
                fa.write('')
        else:
            with open("cardinfo.txt", "a", encoding="utf-8") as fa:
                json.dump(card, fa, default=self.card2Dict)
                fa.write('\n')
# 删
class Del(object):
    def __init__(self):
        pass

    def del_(self,cardId):
        readcard = ReadCard()
        cards = readcard.read()
        for card in cards:
            if cardId == card.cardId:
                cards.remove(card)
                break
        else:
            print("卡号不存在，请重新输入！")
            return False

        appendcard = AppendCard()
        appendcard.append('',w='w')
        for card in cards:
            appendcard.append(card)
        return True
# 测试
def main():
    card = Card('123456', '1234567', 70, '123456','12345678901','False')
    appendCard = AppendCard()
    # appendCard.append(card)
    readCard = ReadCard()
    cards = readCard.read()
    del_ = Del()
    del_.del_(card.cardId)



if __name__ == '__main__':
    main()