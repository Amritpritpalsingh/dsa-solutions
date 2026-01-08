class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start_b = -1
        n = len(s)
        for i in range(n):
            if(s[i]=="b"):
                start_b = i
                break
    
        flag = True
        
        for i in range(i,n):
            if(s[i]=="a"):
                flag = False
                break
        
        return flag
        
