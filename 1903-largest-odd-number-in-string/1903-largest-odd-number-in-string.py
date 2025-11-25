class Solution(object):
    def largestOddNumber(self, num):
        res=""
        num= int(num)
        while(num>0):
            if(num%2!=0):
                res=num
                break
            else:
                num//=10
        return str(res)
      
        