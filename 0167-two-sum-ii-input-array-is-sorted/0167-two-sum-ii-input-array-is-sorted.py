class Solution(object):
    def twoSum(self, nums, tar):
        i = 0
        j = len(nums)-1
        while(i<j):
            summation = nums[i]+nums[j]
            if(summation==tar):
                return [i+1,j+1]
            elif(summation>tar):
                j-=1
            else:
                i+=1
        return [-1,-1]

