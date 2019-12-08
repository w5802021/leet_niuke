import time, functools
def display_time(fun):
    functools.wraps(fun)
    def wrapper(*args, **kw):
        startTime = time.time()
        tmp = fun(*args, **kw)
        endTime = time.time()
        print('%s executed : %s s' % (fun.__name__, float(endTime - startTime )))
        return tmp
    return wrapper

class Trie:
    '''
    字典树知识：
     Trie 树最大优点：利用字符串的公共前缀来减少存储空间与查询时间，从而最大限度地减少无谓的字符串比较
     与哈希表的比较：随着哈希表大小增加，会出现大量的冲突，时间复杂度可能增加到 O(n)，其中 n 是插入的键的数量。
     与哈希表相比，Trie 树在存储多个具有相同前缀的键时可以使用较少的空间。此时 Trie 树只需要 O(m) 的时间复杂度，
     其中 m 为键长。而在平衡树中查找键值需要 O(mlogn) 时间复杂度。

    '''
    # 前缀树初始化
    def __init__(self):
        # 初始化字典树的根节点为空
        self.root={}
        self.end_char = '#'
    #插入
    def insert(self,word):
        node = self.root
        for char in word:
            # 递归建立字典
            node= node.setdefault(char,{})
        node[self.end_char] = self.end_char
    # 搜索
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            # 转移到其它节点搜索
            node = node[char]
        return self.end_char in node

    # 查找满足前缀为word的字符串

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            # 如果当前节点不能满足
            node = node[char]
        return True
if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))


