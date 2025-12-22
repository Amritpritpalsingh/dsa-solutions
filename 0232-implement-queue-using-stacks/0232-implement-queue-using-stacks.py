from Queue import LifoQueue

class MyQueue(object):

    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, x):
        while(self.s1.qsize()):
            self.s2.put(self.s1.get())
        self.s1.put(x)
        while(self.s2.qsize()):
            self.s1.put(self.s2.get())
        
    def pop(self):
        return self.s1.get()
    def peek(self):
        x = self.s1.get()
        self.s1.put(x)
        return x
    def empty(self):
        return self.s1.qsize()==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()