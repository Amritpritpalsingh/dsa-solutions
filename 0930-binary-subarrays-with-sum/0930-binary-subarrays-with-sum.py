class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atMost(goal):
            if goal < 0:
                return 0

            l = 0
            sumi = 0
            count = 0

            for r in range(len(nums)):
                sumi += nums[r]

                while sumi > goal:
                    sumi -= nums[l]
                    l += 1

                count += (r - l + 1)

            return count

        return atMost(goal) - atMost(goal - 1)
