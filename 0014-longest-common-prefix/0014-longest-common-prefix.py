class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        strs.sort()
        for i in range(len(strs[0])):
            map = {}
            for j in range(len(strs)):
                if(strs[j][i] not in map):
                    map[strs[j][i]] = 1
                else:
                    map[strs[j][i]] += 1
                if(len(map)>1):
                    map ={}
                    break
            if(len(map)!=0):
                ans+=strs[j][i]
            else:
                break
        return ans