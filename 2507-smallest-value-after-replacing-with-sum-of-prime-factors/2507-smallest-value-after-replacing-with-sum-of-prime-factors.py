class Solution(object):
    def smallestValue(self, n):
        allFac = [0] * (n + 1)

        for i in range(2, n + 1):
            if allFac[i] == 0:  
                for j in range(i, n + 1, i):
                    x = j
                    while x % i == 0:
                        allFac[j] += i
                        x //= i

        while allFac[n] != n:
            n = allFac[n]

        return n
