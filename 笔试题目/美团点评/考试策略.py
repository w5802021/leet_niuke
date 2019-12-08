n = int(input())
ques = []

for i in range(n):
    p,a,q,b = map(int,input().split())
    ques.append([p,a,q,b])

total = 120
dp = [0] * (total+1)

for i in range(n):
    for j in range(total,ques[i][0]-1,-1):
        if j >= ques[i][2]:
            dp[j] = max(dp[j], dp[j - ques[i][0]] + ques[i][1], dp[j - ques[i][2]] + ques[i][3])

        elif j >= ques[i][0]:
            dp[j] = max(dp[j], dp[j - ques[i][0]] + ques[i][1])
print(dp[total])


