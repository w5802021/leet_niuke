# 思路: 单纯数学规律，从第一个数字开始，每 2m 个数字之和为 m^2，总共有 n/2m 个这样的组合，因此和为 m*n/2
s = input()
n, m = [int(i) for i in s.split(' ')]
print((n*m)//2)
