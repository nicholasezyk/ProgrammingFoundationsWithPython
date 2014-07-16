import time
import random

def NonRigorousCheck(digits):
    try:
        float(digits)
        return True
    except ValueError:
        return False


def RigorousCheck(digits):
    if (NonRigorousCheck(digits)):
        if (len(digits) == 15 or len(digits) == 16):
            if (len(digits) == 15):
                if (digits[0] == '3'):
                    return True
                else:
                    return False
            else:
                if (digits[0] == '4' or digits[0] == '5' or digits[0:4] == '6011'):
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

def DigitSum(digit):
    i = int(digit)
    if (i >= 0 and i <= 4):
        return 2 * i
    elif (i == 5):
        return 1
    elif (i == 6):
        return 3
    elif (i == 7):
        return 5
    elif (i == 8):
        return 7
    elif (i == 9):
        return 9
    


def NonRigorousVerifyLuhn(digits):
    if (NonRigorousCheck(digits)):
        reverse = digits[::-1]
        limit = len(reverse)
        count = 0
        total = 0
        while (count < limit):
            d = reverse[count]
            if (count % 2 == 0):
                total = total + int(d)
            else:
                total = total + DigitSum(d)
            count = count + 1
        if (total % 10 == 0):
            return True
        else:
            return False
    else:
        return False
    

def RigorousVerifyLuhn(digits):
    if (RigorousCheck(digits)):
        reverse = digits[::-1]
        limit = len(reverse)
        count = 0
        total = 0
        while (count < limit):
            d = reverse[count]
            if (count % 2 == 0):
                total = total + int(d)
            else:
                total = total + DigitSum(d)
            count = count + 1
        if (total % 10 == 0):
            return True
        else:
            return False
    else:
        return False

def CheckSumDigit(digits):
    if (NonRigorousCheck(digits)):
        limit = len(digits)
        count = 0
        total = 0
        while (count < limit):
            total = total + int(digits[count])
            count = count + 1
        result = (9 * total) % 10
        return str(result)
    else:
        print("CheckSumDigit error")
        return -1

PROVIDERS = ['AMEX', 'VISA', 'MC', 'DISC']

def generate(num):
    n = str(num)
    print("Please note that this tool is for educational purposes only and the creator of this script would like to note that credit card verification is far more complex than the Luhn algorithm alone, making any attempts at fraud rather futile. Please don't try to break the law using this script.")
    time.sleep(1)
    print("Generating " + n + " credit card numbers 3 seconds from now...")
    time.sleep(3)
    count = 0
    while (count < num):
        rand = random.randrange(4)
        if (rand == 0):
            card = AmexCreditCard()
        elif (rand == 1):
            card = VisaCreditCard()
        elif (rand == 2):
            card = MasterCardCreditCard()
        else:
            card = DiscoverCreditCard()
        print(card.CCnumber + " :: " + card.name + " :: " + "Card number " + str(count + 1))
        count = count + 1
    print(n + " credit card numbers generated!")

class CreditCard():
    def __init__(self, name, short, tag, length):
        self.name = name
        self.short = short
        self.tag = tag
        self.length = length
        self.CCnumber = tag
        while (len(self.CCnumber) < self.length - 1):
            rand_int = random.randrange(10)
            rand_str = str(rand_int)
            self.CCnumber = self.CCnumber + rand_str
        if (length == 15):   
            d = CheckSumDigit(self.CCnumber)
            self.CCnumber = self.CCnumber + d
        if (not RigorousVerifyLuhn(self.CCnumber)):
            ln = self.length - 1
            clip = self.CCnumber[0:ln]
            fulfilled = False
            dig = 0
            while (dig <= 9 and fulfilled == False):
                cand = clip + str(dig)
                if (RigorousVerifyLuhn(cand)):
                    fulfilled = True
                    self.CCnumber = cand
                dig = dig + 1
            if (fulfilled == False):
                if (len(self.CCnumber) != self.length):
                    print("Invalid " + self.name + " number, LENGTH " + len(self.CCnumber) + " (" + self.CCnumber + ")")
                else:
                    print("Invalid " + self.name + " number, LUHN " +  "(" + self.CCnumber + ")")
        
        

class AmexCreditCard(CreditCard):

    def __init__(self):
        CreditCard.__init__(self, 'American Express', 'AMEX', '3', 15)
                    
class VisaCreditCard(CreditCard):

    def __init__(self):
        CreditCard.__init__(self, 'Visa' , 'VISA' , '4', 16)

class MasterCardCreditCard(CreditCard):

    def __init__(self):
        CreditCard.__init__(self, 'MasterCard', 'MC', '5', 16)
        
class DiscoverCreditCard(CreditCard):

    def __init__(self):
        CreditCard.__init__(self, 'Discover', 'DISC', '6011', 16)

generate(random.randrange(100))

    
