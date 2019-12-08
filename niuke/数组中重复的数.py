def duplicate(numbers, duplication):
   '''
    思路：
        数组的长度为 n 且所有数字都在 0 到 n-1 的范围内，我们可以将每次遇到的数进行"归位"，当某个数发现自己的"位置"被相同的数占了，
        则出现重复。扫描整个数组，当扫描到下标为 i 的数字时，首先比较该数字（m）是否等于 i，如果是，则接着扫描下一个数字；如果不是，
        则拿 m 与第 m 个数比较。如果 m 与第 m 个数相等，则说明出现重复了；如果 m 与第 m 个数不相等，则将 m 与第 m 个数交换，
        将 m "归位"，再重复比较交换的过程，直到发现重复的数
   '''
   nums = numbers
   if not nums:
       return False
   for i in range(len(nums)):
       while nums[i] != i:
           if nums[i] == nums[nums[i]]:
               duplication[0] = nums[i]
               print(duplication[0])
               return True
           tmp = nums[i]
           nums[i] = nums[tmp]
           nums[tmp] = tmp
   return False
nums = [2,3,2,4,5,6]
s = [0]
print(duplicate(nums, s))