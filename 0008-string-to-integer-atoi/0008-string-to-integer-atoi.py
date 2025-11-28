class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if(len(s)==0):return 0
        ans = 0
        INT_MIN = -2147483648 
        INT_MAX =  2147483647   
        sing =1
        for i in range(len(s)):
            if(i==0):
                if(s[i]=="-"):
                    sing= -1
                    continue
                else:
                    if(s[i]=="+"):
                        sing = 1
                        continue
                

            if(s[i].isnumeric()):
                ans = ans*10 + int(s[i])
                if(sing==1):
                    if(ans>INT_MAX): 
                        return (INT_MAX)
                        break
                elif(sing==-1):
                    if(-1*ans<INT_MIN):
                        return (INT_MIN)
                        break
            else:
                break

        if(sing == -1):
            ans = ans*-1
        return ans