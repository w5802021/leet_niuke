class Solution:
    def __init__(self):
        self.A = []
        self.B = []
    def push(self, node):
        # write code here
        self.A.append(node)
    def pop(self):
        # return xx
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        first = self.B.pop()
        return first