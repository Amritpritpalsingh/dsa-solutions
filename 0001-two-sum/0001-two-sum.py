class Solution(object):
    def twoSum(self, nums, target):
        
        map = nums[:]
        nums.sort()
        l_ptr = 0
        r_ptr = len(nums)-1
        while(l_ptr<r_ptr):
            summation  = nums[l_ptr]+nums[r_ptr]
            if(summation==target):
                break
            elif(summation>target):
                r_ptr-=1
            else:
                l_ptr+=1
        idx_first = -1
        idx_sec = -1
        for i in range(len(map)):
            if(idx_first==-1 and nums[l_ptr]==map[i]):
                idx_first = i
            elif(idx_sec==-1 and nums[r_ptr]==map[i]):
                idx_sec = i
            if(idx_first!= -1 and idx_sec!= -1):
                break
        return [idx_first,idx_sec]
                