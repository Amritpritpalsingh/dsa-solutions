class Solution(object):
    def maxDepth(self, s):
        cnt = 0
        most = float("-inf")
        for c in s:
            if(c==")"): cnt-=1
            elif(c=="("): cnt+=1
            most = max(most,cnt)
        return most