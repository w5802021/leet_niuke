def main(N,nums):
    MAXI = max(nums)
    sumi = sum(nums)
    # 如果数量最多的某类数的数量大于总树数量的一半
    if ((sumi%2 == 0) and (MAXI > sumi//2)) or ((sumi%2 == 1) and (MAXI > sumi//2 + 1)):
        print('-')
    else:
        result = [0]
      # 遍历每棵树
        for i in range(sumi):
            if MAXI > sumi/2:
                maxind = nums.index(MAXI)
                result.append(maxind+1)
                nums[maxind] = nums[maxind] - 1
            else:
              # 尝试种植下一棵与res最近种的树品种不同的树，如果与前一棵树相同，则选择另外一种
                for j in range(N):
                    if (nums[j] != 0) and (j+1 != result[-1]) :
                        result.append(j+1)
                        nums[j] = nums[j] - 1
                        break
        # 每次迭代要更新nums的值
            MAXI = max(nums)
            sumi = sum(nums)
        result.pop(0)
        str1 = ''
        for i in result:
            str1 = str1 +' ' +str(i)
        return str1.lstrip(' ')

# def main(N,nums):
#   MAXI = max(nums)
#   sumi = sum(nums)
#   # guo
#   if ((sumi % 2 == 0) and (MAXI > sumi // 2)) or ((sumi % 2 == 1) and (MAXI > sumi // 2 + 1)):
#       print('-')
#   else:
#       result = ['start']
#       for i in range(sumi):
#           if MAXI > sumi/2:
#               Mindex = nums.index(MAXI)
#               result = result + [Mindex+1]
#               nums[Mindex] = nums[Mindex] - 1
#           else:
#               for j in range(N):
#                   if (nums[j] != 0) and (j+1 != result[-1]) :
#                       result = result + [j+1]
#                       nums[j] = nums[j] - 1
#                       break
#           MAXI = max(nums)
#           sumi = sum(nums)
#       del result[0]
#       result = str(result).replace('[','')
#       result = result.replace(']','')
#       result = result.replace(',','')
#       return result
if __name__ == '__main__':
    # a = int(input())
    # nums = [int(c) for c in input().split()]
    a = 3
    nums =[4,2,1]
    print(main(a,nums))