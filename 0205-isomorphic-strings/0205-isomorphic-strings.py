class Solution(object):
    def isIsomorphic(self, s, t):
        mapf ={}
        mapb = {}
        for i in range(len(s)):
            if((s[i] in mapf and (mapf[s[i]]!=t[i])) or (t[i] in mapb and (mapb[t[i]]!=s[i]))):
                return False
                
            mapf[s[i]]=t[i]
            mapb[t[i]]=s[i]
        return True
