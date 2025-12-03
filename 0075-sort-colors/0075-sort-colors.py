class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mid , high , low =0,n-1,0
        while(mid<=high):
            if(nums[mid]==0):
                nums[mid],nums[low] = nums[low],nums[mid]
                mid+=1
                low+=1
            elif(nums[mid]==1): mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1 