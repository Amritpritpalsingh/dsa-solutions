class Solution(object):
    def hammingDistance(self, x, y):
        n = x^y
        steps = 0
        for i in range(31):
            if(n&(1<<i)):
                steps+=1
            
        return steps
