class Solution(object):
    def largestOddNumber(self, num):
        res=""
        x= int(num)
        while(x>0):
            if(x%2!=0):
                res=x
                break
            else:
                x//=10
        return str(res)
      
        