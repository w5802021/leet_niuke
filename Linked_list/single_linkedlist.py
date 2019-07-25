import math
class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):              #自定义链表抛出异常错误
    pass

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self,elem):             #在最前面插入元素
        self._head = LNode(elem,self._head)

    def pop(self):                     #弹出最前面的元素
        if self._head is None:
            raise LinkedListUnderflow('in pop')

        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self,elem):         #在最后插入元素
        if self._head is None:
            self._head = LNode(elem)
            return

        p = self._head
        while p.next is not None:
            p = p.next

        p.next = LNode(elem)

    def pop_last(self):               #在最后弹出元素
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')

        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self,pred):        #在列表中找到满足给定pred函数条件的第一个值
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end = '')
            if p.next is not None:
                print(', ',end = '')
            p = p.next
        print('')

    def elements(self):            #用生成器函数实现对象的一个迭代器
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self,pred):         ##在列表中找到满足给定pred函数条件的所有值  (find的升级功能)
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

class LList1:                   #增加尾指针  后端插入提高的效率
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self,elem):             #在最前面插入元素
        if self._head is None:
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self,elem):                 #后端插入提高的效率
        if self._head is None:
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')

        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        self._rear = p
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
    list1 = LList()
    # for i in range(10):
    #     list1.prepend(i)
    # for i in range(11,20):
    #     list1.append(i)
    # list1.pop()
    # list1.pop_last()
    # list1.printall()
    #
    # for x in list1.elements():
    #     print(x)

    # for i in list([2,4,6,2,2]):
    #     list1.append(i)
    #
    # print(list1.find(lambda x: x < 5))
    # for i in list1.filter(lambda x:x<5):
    #     print(i)

    list2 = LList1()
    for i in range(11,20):
        list2.append(i)
    list2.printall()
