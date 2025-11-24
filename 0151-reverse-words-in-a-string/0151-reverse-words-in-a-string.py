class Solution(object):
    def reverseWords(self, s):
        stack = []
        el = ""
        for i in range(len(s)):
            if(s[i]!=" "):
                el+=s[i]
            elif(s[i]==" " and len(el)!=0):
            
                stack.append(el)
                el=""
                
        if(s[-1]!=" "):
            stack.append(el)
        res  = ""

        for i in range(len(stack)-1,-1,-1):
            if(i!=0):
                res+=stack[i]+" "
            else:
                res+=stack[i]
        return res