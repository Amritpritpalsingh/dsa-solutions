class Solution(object):
    

    def maximumCount(self, nums):
        if(nums[0]>0 or nums[-1]<0):return len(nums)
        n = len(nums)

       
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                low = mid + 1
            else:
                high = mid
        neg_count = low

       
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= 0:
                low = mid + 1
            else:
                high = mid
        pos_count = n - low

        return max(neg_count, pos_count)

        
    