class Solution(object):
    def checkPerfectNumber(self, num):
        if(num==1):
            return false
        sumi = 1
        for i in range(2,int(num**.5)+1):
            if(num%i==0):
                sumi+=i+(num//i)
        if(sumi==num):
            return True
        return False
            