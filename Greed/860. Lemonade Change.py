
def lemonadeChange(bills):
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if not five: return False
            five -= 1
            ten += 1
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


if __name__ == '__main__':
    l = [5,5,5,5,20,20,5,5,20,5]
    print(lemonadeChange(l))