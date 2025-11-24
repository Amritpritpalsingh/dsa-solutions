class Solution(object):
    def removeOuterParentheses(self, s):
        j = 0
        output = ""
        cnt = 0
        while(j<len(s)-1):
            if(s[j]==")"):
                cnt-=1
            if(cnt!=0):
                output+=s[j]
            if(s[j]=="("):
                cnt+=1
            j+=1
        return output
   
        