class Solution(object):
    def maxScore(self, nums, k):
        max_sum = 0
        l_sum = 0
        r_sum = 0
        for i in range(k):
            l_sum+=nums[i]
        max_sum = l_sum
        last_el = len(nums) - 1
        for i in range(k):
            l_sum -= nums[k-i-1]
            r_sum += nums[last_el]
            last_el-=1
            max_sum = max(max_sum,l_sum+r_sum)
        return max_sum  

        