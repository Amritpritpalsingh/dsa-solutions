class Solution(object):
    def largestEven(self, s):
        if int(s[-1]) % 2 == 0:
            return s
        if len(s) == 1:
            return ""
        
        ans = ""
        n = len(s)
        i = 0
        
        for i in range(n):
            if int(s[n - 1 - i]) % 2 != 0:
                continue
            else:
                break
        
        if i == n:
            return ""
        
        for j in range(n - i):
            ans += s[j]
        if(int(ans)%2==0):
            return ans
        else:
            return ""
