n,m = map(int,input().split())
nums = []
for i in range(m):
    nums.append(int(input()))

class sol:
    def __init__(self):
        self.seen = set()

    def dfs(self,nums,n,m,pos,step):

        if step == m:
            if pos not in self.seen:
                self.seen.add(pos)
            return

        if 1 <= pos + nums[step]  <= n:
            a = pos + nums[step]
            self.dfs(nums,n,m,a,step+1)
        if 1 <= pos - nums[step]  <= n:
            b = pos - nums[step]
            self.dfs(nums,n,m,b,step+1)

        return

    def main(self):
        for pos in range(1,n+1):
            self.dfs(nums,n,m,pos,0)
        print(len(self.seen))
test = sol()
test.main()

s = list(input())
dic = set(s)
maxx = 0
for c in dic:
    if s.count(c) > maxx:
        maxx = s.count(c)

print(maxx)