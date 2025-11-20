class Solution(object):
    def maxProduct(self, nums):
        m = nums[0]     # max product found
        p = 1           # running product

        # Pass 1: left to right
        for x in nums:
            p *= x
            m = max(m, p)
            if p == 0:   # reset product if zero
                p = 1

        # Pass 2: right to left
        p = 1
        for x in reversed(nums):
            p *= x
            m = max(m, p)
            if p == 0:
                p = 1

        return m
