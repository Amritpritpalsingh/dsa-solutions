class Solution(object):
    def beautySum(self, s):
        ans = 0
        for i in range(len(s)):
            map = {}
            for j in range(i,len(s)):
                if(s[j] not in map):map[s[j]]=1
                else: map[s[j]]+=1
                ans+=max(map.values())-min(map.values())
        return ans