class Solution(object):
    def shuffle(self, nums, n):
        ans = [] 
        for i in range(len(nums)//2):
            ans.extend([nums[i],nums[i+n]])
        return ans
           