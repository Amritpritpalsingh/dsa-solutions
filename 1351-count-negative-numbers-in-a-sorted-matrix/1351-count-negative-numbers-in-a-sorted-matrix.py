class Solution(object):
    def lb(self,nums):
        n = len(nums)
        low, high = 0, n

        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= 0:
                low = mid + 1
            else:
                high = mid
        if(low==n):
            return 0
        return n-low
    def countNegatives(self, grid):
        cnt = 0 
        for i in range(len(grid)):
            cnt+=self.lb(grid[i])
        return cnt
        