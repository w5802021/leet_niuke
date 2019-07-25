class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):              #自定义链表抛出异常错误
    pass

class LCList:              ##循环链表类
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):             #在最前面插入元素
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def pop(self):                     #弹出最前面的元素
        if self._rear is None:
            raise LinkedListUnderflow('in pop')

        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next

        return p.elem

    def append(self,elem):         #在最后插入元素
        self.prepend(elem)
        self._rear = self._rear.next

    # def pop_last(self):               #在最后弹出元素
    #     if self._rear is None:
    #         raise LinkedListUnderflow('in pop')
    #
    #     p = self._rear.next
    #     if self._rear is p:
    #         self._rear = None
    #     else:
    #         while p.next.next is not self._rear:
    #             p = p.next
    #         p = p.next.next
    #
    #     return p.elem

    def printall(self):
        if self.is_empty():
            return

        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

if __name__ == '__main__':
    list1 = LCList()
    for i in range(10):
        list1.prepend(i)
    for i in range(11,20):
        list1.append(i)
    list1.pop()

    # list1.printall()