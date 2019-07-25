from itertools import combinations
def letterCombinations(digits):
    dic = {2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'],
           7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']}
    dic1 = {"2": "abc","3": "def","4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
    if digits == '':
        return []
    res = ['']
    for i in digits:
        tmp = []
        for j in dic[int(i)]:
            for k in res:
                tmp.append( k+j )
        res = tmp
    return res

def letterCombinations2(digits):
    def dfs(res, dic, digits, cur):
        if not digits:
            res.append(cur)
            return
        for c in dic[digits[0]]:
            dfs(res, dic, digits[1:], cur + c)

    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    cur = ""
    dfs(res, dic, digits, cur)
    return res

if __name__ == '__main__':
    s = "23"
    print(letterCombinations2(s))