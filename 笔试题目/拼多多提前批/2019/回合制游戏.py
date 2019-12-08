def main(hp, normalatt, buffatt):
    if normalatt > buffatt // 2:
        if hp % normalatt == 0:
            count = hp // normalatt
        else:
            count = hp // normalatt + 1
        return count
    else:
        count1 = 2 * (hp // buffatt)
        remain = hp - (count1 // 2) * buffatt
        if remain > normalatt:
            count1 += 2
        elif remain == 0:
            count1 += 0
        else:
            count1 += 1
    return count1


if __name__ == '__main__':
    hp = int(input())
    normalatt = int(input())
    buffatt = int(input())
    print(main(hp, normalatt, buffatt))
