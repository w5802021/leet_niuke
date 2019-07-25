class DLNode:
    def __init__(self,elem,prev = None,next_=None):
        self.elem = elem
        self.next = next_
        self.prev = prev    #多一个前向指针

class LinkedListUnderflow(ValueError):              #自定义链表抛出异常错误
    pass

class DLList:
    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self,elem):
        p = DLNode(elem, None, self._head)  #激活头指针
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self,elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow(' in pop of DLList')

        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow(' in pop_last of DLList')

        e = self._head.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end = '')
            if p.next is not None:
                print(', ',end = '')
            p = p.next
        print('')

if __name__ == '__main__':
    list1 = DLList()
    for i in range(11,20):
        list1.prepend(i)
    list1.pop_last()
    list1.printall()