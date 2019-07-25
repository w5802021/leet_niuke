######理解题意：两字符串完全相等，则不可能有最长特殊子序列，长度相同，取任意一个即可，长度不同，取长的那个字符串即可####

def findLUSlength1(a, b):
    if a == b:
        return -1

    return max(len(a), len(b))

def findLUSlength2(a, b):
    if a == b:
        return -1

    return max(len(a), len(b))

################################522#############################
def findLUSlength3(strs):
    def subseq(w1, w2):
        # True iff word1 is a subsequence of word2.
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:   #i用于记录w1中的元素是否在w2中全部出现过   这里添加i < len(w1)
                i += 1
        return i == len(w1)                  #当i = len(w1) 说明w1中的元素按顺序地在w2中出现 即w1是w2的子序列

    A = strs  # 采用降序排列，找到此字符串则为最长字符串 速度最快
    A.sort(key = len, reverse = True)
    for i, word1 in enumerate(A):
        if all(not subseq(word1, word2) for j, word2 in enumerate(A) if i != j):   #当word1都不是除word1以外的strs元素中的子序列时，输出该word1为最长特殊子序列
            return len(word1)
    return -1

if __name__ == '__main__':
    a,b = "aba", "cdc"
    # print(findLUSlength1(a,b))
    print(findLUSlength3(["aba", "cdc", "eaedfg"]))