class Solution(object):
    def singleNumber(self, nums):
        XOR = 0
        for i in nums:
            XOR^= i
        return XOR
        