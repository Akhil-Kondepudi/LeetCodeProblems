import sys
class MinStack(object):

    stack = []
    minstack = []
    small = sys.maxint
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.small = sys.maxint

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.small = val if self.small > val else self.small
        self.minstack.append(self.small)

    def pop(self):
        """
        :rtype: None
        """
        out = self.stack.pop()
        self.minstack.pop()
        if len(self.minstack) > 0:
            self.small = self.minstack[-1]
        else:
            self.small = sys.maxint
        return out

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.small
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()