import sys

def main(a,nums):
    c = a+nums
    return c

if __name__ == '__main__':
    # 1
    a = int(input())
    nums = [int(c) for c in input().split()]
    print(main(a,nums))
    # 2
    res = [int(c) for c in input().split()]
    n, k = res[0], res[1]
    n, k = map(int, input().split())
    nums = [int(c) for c in input().split()]
    print(main(n, k, nums))