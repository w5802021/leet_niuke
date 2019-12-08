# python3
def main():
    case = int(input())
    for c in range(case):
        n = int(input())
        golds = [int(c) for c in input().split()]

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        sum = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + golds[i - 1]
            dp[i][i] = golds[i - 1]
        #
        for j in range(n):
            for i in range(1, n):
                if i + j <= n:
                    dp[i][i + j] = sum[i + j] - sum[i - 1] - min(dp[i + 1][i + j], dp[i][i + j - 1])
        print ('Case #%d: %d %d'%(c + 1, dp[1][n], sum[n] - dp[1][n]))

if __name__ == '__main__':
    main()

# python2的输入
# n = int(raw_input())
# a = [int(i) for i in raw_input().split()]
# dp = [1]
# for i in range(1,n+1):
#     d = 0
#     col =  [0]*10
#     for j in range(i):
#         col[a[i - j - 1]] += 1
#         if(col[a[i - j - 1]] > 1):
#             break
#         d += dp[i-1-j]
#     dp.append(d)
# print dp[-1] % 1000000007

'''
C++输入输出
#include  <iostream> 
using namespace std;
int main()
{
    int N, M;
    // 每组第一行是2个整数，N和M，至于为啥用while，因为是多组。
    while(cin>> N >> M) {
      cout << N << " " << M << endl;
      // 循环读取“接下来的M行”
      for (int i=0; i<M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        cout << a << " " << b << " " << c << endl;
      }
    }
    return 0;
}

'''