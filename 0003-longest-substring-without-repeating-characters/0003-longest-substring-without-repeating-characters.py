class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        map = {} 
        lenm = 0 
        for r in range(len(s)):
            if(s[r] not in map or map[s[r]]<l):
                map[s[r]] = r
                lenm = max(lenm,r-l+1)
            else:
                l = map[s[r]]+1
            map[s[r]] = r
        return lenm

        