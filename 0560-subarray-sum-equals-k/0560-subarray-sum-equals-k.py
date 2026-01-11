class Solution(object):
    def subarraySum(self, nums, k):
        from collections import defaultdict
        map = defaultdict(int)
        map[0] = 1
        cnt = 0
        summation = 0
        for i in range(len(nums)):
            summation+=nums[i]
            remain = summation-k
            cnt+=map[remain]
            map[summation]+=1
        return cnt

        