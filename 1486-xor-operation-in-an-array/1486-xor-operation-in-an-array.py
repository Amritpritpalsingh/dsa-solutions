class Solution(object):
    def xorOperation(self, n, start):
        XOR = 0
        for i in range(n):
            XOR^=(start+2*i)

        return XOR
        