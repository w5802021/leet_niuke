n = int(input())
nums = list(input().split())

for i in range(n):
    if nums[i] in ['+','-','*','/']:
        j = i
        break

for i in range(len(nums)):

    if nums[i] in ['+','-','*','/']:
        # new存改变顺序后的算术表达式，nums仍为之前未交换的算术表达式，后面判断两者运算结果是否相等
        new = nums[:]
        # 带条件的插入排序
        for j in range(i,0,-2):
            if int(new[j+1]) > int(new[j-1]):
                break
            # 如果后面的数字比前面大
            new[j+1],new[j-1] = new[j-1],new[j+1]
            # 直接由字符串计算公式 算术结果
            if eval(''.join(new)) == eval(''.join(nums)):
                nums = new[:]
            else:
                break
print(' '.join(nums))

