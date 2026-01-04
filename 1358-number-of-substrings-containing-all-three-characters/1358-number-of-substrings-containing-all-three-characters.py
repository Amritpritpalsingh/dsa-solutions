class Solution(object):
    def numberOfSubstrings(self, s):
        lastseen = [-1]*3
        cnt = 0
        for i in range(len(s)):
            lastseen[ord(s[i])-ord("a")] = i
            if(lastseen[0]!= -1 and lastseen[1]!= -1 and lastseen[2]!= -1):
                cnt += min(lastseen) + 1
        return cnt