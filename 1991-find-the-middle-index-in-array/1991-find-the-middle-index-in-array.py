class Solution(object):
    def pre_sum(self, nums):
        n = len(nums)
        pre_sum = [0] * n
        pre_sum[0] = nums[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
        return pre_sum

    def findMiddleIndex(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        pre_sum_array = self.pre_sum(nums)
        total_sum = pre_sum_array[-1]

        for i in range(n):
            left_sum = pre_sum_array[i - 1] if i > 0 else 0
            right_sum = total_sum - pre_sum_array[i]
            if left_sum == right_sum:
                return i

        return -1
