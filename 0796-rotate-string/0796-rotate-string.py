class Solution(object):
    def rotateString(self, s, goal):
        if(len(s)!=len(goal)):return False
        goal +=goal
        l = len(s)

        for i in range(len(s)):
            ans = ""
            for j in range(i,l):
                ans+=goal[j]
            l+=1
            if(ans==s):
                return True
                break
        return False
            