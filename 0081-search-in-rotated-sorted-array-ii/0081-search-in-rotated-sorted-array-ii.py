class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def find(nums,x,n):
            low = 0
            high = n-1
            while(low<=high):
                mid = (low) + (high-low)//2
                if(nums[mid]==x):
                    return True
                elif(nums[mid]==nums[low] and nums[mid]==nums[high]):
                    high -=1
                    low+=1
                    continue
                elif(nums[low]<=nums[mid]):
                    if(nums[low]<=x and nums[mid]>=x ):
                        high = mid - 1
                    else:
                        low = mid + 1
                elif(nums[high]>=nums[mid]):
                    if(nums[mid]<=x and nums[high]>=x):
                        low = mid +1
                    else:
                        high = mid - 1
            return False
        return find(nums,target,len(nums))

        