
s = 'aabccb'
ans = 0
mp = dict()
cur = 0
s = list(map(ord,s))
'''
思路：字典mp每个对应的key存储遍历到目前该字符为止，该字符串中偶数串的个数
'''
for num in s:
      # get()方法，第二个参数，若不能找到对应的key，则返回0
      mp[cur] = mp.get(cur, 0)+1
      a = 1 << num
      cur ^= 1<<num
      ans += mp.get(cur, 0)
print (ans)

