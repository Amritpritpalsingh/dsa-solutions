class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(2*len(nums)):
            ans.append(nums[i%len(nums)])
        return ans
        