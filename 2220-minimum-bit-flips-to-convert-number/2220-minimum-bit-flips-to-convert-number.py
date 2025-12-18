class Solution(object):
    def minBitFlips(self, start, goal):
        bits = start^goal
        steps = 0
        for i in range(31):
            if(bits&(1<<i)):
                steps+=1
        return steps


