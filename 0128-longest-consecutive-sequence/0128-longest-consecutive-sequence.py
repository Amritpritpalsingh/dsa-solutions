class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        longest = 1
        if(len(nums)==0): return 0
        for i in s:
            if(i-1 not in s):
                count = 1
                x = i
                while(x+1 in s):
                    x=x+1
                    count+=1
                longest = max(longest,count)
        return longest