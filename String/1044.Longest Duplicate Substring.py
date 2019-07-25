def longestDupSubstring(S):
    import functools
    A = [ord(c) - ord('a') for c in S]
    base = 26
    mod = 2 ** 63 - 1
    n = len(S)
    ###rabin-Karp 指纹字符串查找算法
    def rabinKarp(k):
        p = pow(base, k, mod)
        cur = functools.reduce(lambda x, y: (x * base + y) % mod, A[: k])
        seed = {cur}
        for index in range(k, n):
            cur = (cur * base + A[index] - A[index - k] * p) % mod
            if cur in seed:
                return index - k + 1
            seed.add(cur)
        return -1
    ###二分查找
    low, high = 0, n
    res = 0
    while low < high:
        mid = (low + high + 1) // 2
        pos = rabinKarp(mid)
        if pos != -1:
            low = mid
            res = pos
        else:
            high = mid - 1
    return S[res: res + low]

if __name__ == '__main__':
    str = "banana"
    print(longestDupSubstring(str))