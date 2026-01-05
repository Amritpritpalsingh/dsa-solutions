class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.cnt(nums,k)-self.cnt(nums,k-1)

    def cnt(self,nums,k):
        sub_arrays = 0
        map = {}
        l_ptr = 0
        for r_ptr  in range(len(nums)):
            if(nums[r_ptr] not in map):
                map[nums[r_ptr]] = 1
            else:
                map[nums[r_ptr]]+=1
            while(len(map)>k):
                map[nums[l_ptr]]-=1
                if(map[nums[l_ptr]]==0): del map[nums[l_ptr]]
                l_ptr+=1
        
            if(len(map)<=k):
                sub_arrays += r_ptr - l_ptr + 1
        return sub_arrays


