class Solution(object):
    def largestAltitude(self, gain):
        high_alti = 0
        pre_sum = 0
        for al in gain:
            pre_sum += al
            high_alti =  max(high_alti,pre_sum)
        return high_alti