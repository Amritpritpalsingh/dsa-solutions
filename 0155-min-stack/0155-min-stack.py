from Queue import LifoQueue
class MinStack(object):

    def __init__(self):
        self.st = LifoQueue()
        self.min = float("inf")
        
    def push(self, val):
        if(self.st.qsize()==0):
            self.min = val
            self.st.put(val)
        else:
            if(val>self.min):
                self.st.put(val)
            else:
                self.st.put(((2*val)-self.min))
                self.min = val
    def pop(self):
        if(self.st.qsize()==0):
            return 
        x  = self.st.get()
        if(x<self.min):
            self.min = 2*self.min-x
        return self.min
        

    def top(self):
        if(self.st.qsize()==0):
            return 
        x = self.st.queue[-1]
        if(x>self.min):
            return x
        return self.min


    def getMin(self):
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()