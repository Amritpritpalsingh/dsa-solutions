class Solution(object):
    def waysToSplitArray(self, nums):
        n = len(nums)
        ps = [0]*n
        ps[0] = nums[0]
        for i in range(n):
            ps[i] = ps[i-1]+nums[i]
            
        split_idx = 0
        total_sum = ps[-1]
        for i in range(n-1):
            left_sum = ps[i]
            right_sum = total_sum - ps[i]
            if(left_sum>=right_sum):
                split_idx+=1
        return split_idx
    
        