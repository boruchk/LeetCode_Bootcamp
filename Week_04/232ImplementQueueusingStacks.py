class MyQueue(object):

    def __init__(self):
        self.temp = []
        self.real = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.temp.append(x)
        self.real = []
        for x in self.temp[::-1]:
            self.real.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.real:
            return None
        self.temp.pop(0)
        return self.real.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.real:
            return None
        return self.real[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.real
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()