class Solution(object):
    def myPow(self, x, n):
        ans = 1
        sign = False
        if(n<0):
            sign = True
            n = abs(n)
        while(n>0):
            if(n&1):
                ans*=x
                n=n-1
            else:
                n=n//2
                x=x*x
        if(sign is True):
            return 1/ans
        return ans
        
        