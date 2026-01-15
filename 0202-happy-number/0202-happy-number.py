class Solution(object):
    def sum_of_square(self,n):
        summation = 0
        while(n>0):
           summation += (n%10)**2
           n//=10
        return summation

    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sum_of_square(n)
            if(n==1):return True
        return False
        