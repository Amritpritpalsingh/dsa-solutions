class Solution(object):
    def numberOfSubarrays(self, nums, goal):
        def atMost(goal):
            if goal < 0:
                return 0

            l = 0
            sumi = 0
            count = 0

            for r in range(len(nums)):
                sumi += nums[r]%2

                while sumi > goal:
                    sumi -= nums[l]%2
                    l += 1

                count += (r - l + 1)

            return count

        return atMost(goal) - atMost(goal - 1)