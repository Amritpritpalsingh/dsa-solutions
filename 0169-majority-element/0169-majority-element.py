class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count =0
        el=nums[0]
        for i in range(len(nums)):
            if(count==0):
                count+=1
                el=nums[i]
            elif(nums[i]==el): count+=1
            else: count-=1
        isMax = 0
        for i in nums:
            if(i==el):isMax+=1
        
        if(isMax>=len(nums)/2):
            return el
        else: return -1
        