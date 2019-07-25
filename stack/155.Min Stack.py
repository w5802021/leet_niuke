class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []

    def push(self, x):
        if not self.item:
            self.item.append([x, x])
        else:
            self.item.append([x, min(self.item[-1][1], x)])

    def pop(self):
        self.item.pop()

    def top(self) :
        return self.item[-1][0]

    def getMin(self):
        return self.item[-1][1]
