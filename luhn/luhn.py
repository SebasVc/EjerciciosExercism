import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')
        self.card_num = self.card_num[::-1]
    def valid(self):
        regEx = re.compile(r'^[\d]+$')
        if len(self.card_num) <= 1:
            return False;
        elif regEx.match(self.card_num):
            summ=0
            count=0
            for n in self.card_num:
                num = int(n)
                if count%2==1:
                    num = num*2
                    if num >=10:
                        num-=9
                summ+=num
                count+=1

            return summ%10 == 0

        return False