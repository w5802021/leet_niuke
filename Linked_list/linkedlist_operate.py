
class LNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    #链表初始化函数, 方法类似于尾插
    def initList(self, val):
        #创建头结点
        self.head = LNode()
        p = self.head
        #逐个为 val 内的数据创建结点, 建立链表
        for i in val:
            node = LNode(i)
            p.next = node
            p = p.next

        return self.head    #将列表转化为链表结构后要返回链表的头指针

    #链表判空
    def isEmpty(self):
        if self.head.next == 0:
            print ("Empty List!")
            return 1
        else:
            return 0

    #取链表长度
    def getLength(self):
        if self.isEmpty():
            exit(0)
        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    #输出链表
    def outll(self,res):
        p = res
        while p is not None:
            print(p.val, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    #链表插入数据函数
    def insertElem(self, key, index):
        if self.isEmpty():
            exit(0)
        if index<0 or index>self.getLength()-1:
            print ("\rKey Error! Program Exit.")
            exit(0)
        p = self.head
        i = 0
        while i<=index:
            pre = p
            p = p.next
            i += 1
        #遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = LNode(key)
        pre.next = node
        node.next = p

    #链表删除数据函数
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index<0 or index>self.getLength()-1:
            print ("\rValue Error! Program Exit.")
            exit(0)

        i = 0
        p = self.head
        #遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i==index:
                pre.next = p.next
                p = None
                return 1

        #p的下一个结点为空说明到了最后一个结点, 删除之即可
    def create_linklist(self):
        i = 1
        head = LNode()
        head.next = None
        tmp = None
        cur = head

        while i < 8:
            tmp = LNode()
            tmp.val = i
            tmp.next = None
            cur.next = tmp
            cur = tmp
            i += 1

if __name__ == '__main__':
    # 初始化链表与数据
    val = [1, 2, 3, 4, 5]
    # l = LinkList()
    # l.initList(val)
    # l.traveList()
    #
    # # 插入结点到索引值为3之后, 值为666
    # l.insertElem(666, 3)
    # l.traveList()
    #
    # # 删除索引值为4的结点
    # l.deleteElem(4)
    # l.traveList()


