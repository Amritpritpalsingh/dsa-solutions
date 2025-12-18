class Solution(object):
    def subsets(self, nums):
        subset = 1<<len(nums)
        res = []
        for ss in range(subset):
            ans  = []
            for el in range(ss):
                if(ss&(1<<el)):
                    ans.append(nums[el])
            res.append(ans)
        return res



        