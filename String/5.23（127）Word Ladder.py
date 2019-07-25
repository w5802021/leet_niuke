from collections import deque,defaultdict
###方法一：贪心BFS算法（非最短路径）
class Qitem():
    def __init__(self,word,lens):
        self.word = word
        self.lens = lens

def isdiff(str1,str2):
    diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def shortestchain(D,start,target):
    Q = deque()
    item = Qitem(start,1)
    Q.append(item)

    while len(Q) > 0:
        curr = Q[0]
        Q.pop()
        for it in D:
            temp = it
            if isdiff(curr.word,temp):
                item.word = temp
                item.lens += 1
                Q.append(item)
                D.remove(temp)
                if temp == target:
                    return item.lens
    return 0

###方法二：BFS
def shortestchain1(wordList,beginWord,endWord):
    '''
    思路：双向BFS
    '''

    if not beginWord or not endWord or not wordList or endWord not in wordList:
        return 0
    n = len(beginWord)
    wordList_dict = defaultdict(list)
    for word in wordList:
        for i in range(n):
            wordList_dict[word[:i] + '*' + word[i + 1:]].append(word)
    levels_l = [(beginWord, 1)]
    levels_2 = [(endWord, 1)]
    used_dict1 = {beginWord: 1}
    used_dict2 = {endWord: 1}

    def visit(n, used_dict1, used_dict2, levels):
        word1, level = levels.pop(0)
        for i in range(n):
            mid_word = word1[:i] + '*' + word1[i + 1:]
            for word in wordList_dict[mid_word]:
                if word not in used_dict1:
                    if word in used_dict2:
                        return level + used_dict2[word]
                    levels.append((word, level + 1))
                    used_dict1[word] = level + 1
                else:
                    if word in used_dict2:
                        return used_dict1[word] + used_dict2[word]
        return 0

    while levels_l and levels_2:
        cn1 = visit(n, used_dict1, used_dict2, levels_l)
        if cn1:
            return cn1
        cn2 = visit(n, used_dict2, used_dict1, levels_2)
        if cn2:
            return cn2
    return 0

def shortestchain2(wordList,beginWord,endWord):

    if endWord not in wordList:
        return 0
    l = len(endWord)
    ws = set(wordList)

    head = {beginWord}
    tail = {endWord}
    tmp = list('abcdefghijklmnopqrstuvwxyz')
    res = 1
    while head:
        if len(head) > len(tail):
            head, tail = tail, head

        q = set()
        for cur in head:
            for i in range(l):
                for j in tmp:
                    word = cur[:i] + j + cur[i + 1:]
                    if word in tail:
                        return res + 1
                    if word in ws:
                        q.add(word)
                        ws.remove(word)
        head = q
        res += 1

    return 0          #对本测试例出现错误  待调试

if __name__ == '__main__':
    D = ['pooN','pbcc','zamc','poIc','pbca','pbIc','poIN']
    start = 'TooN'
    target = 'pbca'
    print(shortestchain1(D,start,target))


