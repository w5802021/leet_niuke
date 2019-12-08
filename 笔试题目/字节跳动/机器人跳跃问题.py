n = int(input())
nums = [int(c) for c in input().split()]

def fun(val):
    power = val
    for i in nums:
        if power > i:
            power += power - i
        elif power < i:
            power -=  i - power
    return power

def main(nums):
    low = 0
    high = max(nums)

    while low < high:
        mid = (low + high)//2
        res = fun(mid)
        if res == 0:
            return mid
        elif res > 0:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
    print(main(nums))