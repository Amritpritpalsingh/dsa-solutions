class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN_INT32 = -2**31       
        MAX_INT32 = 2**31 - 1
        isNeg = False
        if(x<0):
            isNeg = True
            x=-(x)

        y = str(x)
        i=0
        y = int(y[::-1])
        if (MIN_INT32>y or y>MAX_INT32):
            return  0
        
        if(isNeg):
            y=-(y)
      
        return y