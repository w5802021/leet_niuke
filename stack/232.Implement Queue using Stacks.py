class MyQueue():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.itema = []
        self.itemb = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.itema.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.itemb:
            while self.itema:
                self.itemb.append(self.itema.pop())
        first = self.itemb.pop()
        return first

    def peek(self):
        """
        Get the front element.
        """
        if not self.itemb:
            while self.itema:
                self.itemb.append(self.itema.pop())
        return self.itemb[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.itema) == 0 and len(self.itemb) == 0