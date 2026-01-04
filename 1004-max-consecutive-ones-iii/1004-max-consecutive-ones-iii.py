class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        l = 0
        zero = 0
        ans = 0
        for i in range(n):
            if(nums[i]==0):zero+=1
            if(zero>k):
                if(nums[l]==0):zero-=1
                l+=1
            if(zero<=k):
                ans  = max(ans,i-l+1)
        return ans
            
    

