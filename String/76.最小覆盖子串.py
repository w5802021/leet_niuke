from collections import Counter,defaultdict
def minWindow(s, t):
    '''
    :param s:
    :param t:
    :return:
    '''

    t = Counter(t)
    lookup = defaultdict(int)
    # start，end分别表示动态滑窗的起始点
    start = 0
    end = 0
    min_len = float("inf")
    res = ""
    while end < len(s):
        lookup[s[end]] += 1
        end += 1
        # print(start, end)
        while all(map(lambda x: lookup[x] >= t[x], t.keys())):
            if end - start < min_len:
                res = s[start:end]
                min_len = end - start
            lookup[s[start]] -= 1
            start += 1
    return res

def minWindow1(s, t):
    # mem为t的字符计数器
    mem = defaultdict(int)
    for char in t:
        mem[char] += 1
    t_len = len(t)

    minL, minR = 0, float('inf')
    l = 0
    for r, ch in enumerate(s):
        # 经过此步操作后，mem中包含t的key的键值为0，其余的s中遍历过的字符但是不在t中的键值变为负数（这里我们值关系t中对应的值
        # 在mem中的计数情况，其它的不需要过多考虑）
        if mem[ch] > 0:
            t_len -= 1
        mem[ch] -= 1
        # 当子串满足要求，mem记录的是满足存在子串的滑窗中的字符个数
        if t_len == 0:
            while mem[s[l]] < 0:
                mem[s[l]] += 1
                l += 1
            # 存下当前动态滑窗在字符串中的索引
            if r - l < minR - minL:
                minL, minR = l, r

            # 调整滑窗的前向索引
            mem[s[l]] += 1
            t_len += 1
            l += 1
    return '' if minR == float('inf') else s[minL:minR + 1]

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow1(s, t))