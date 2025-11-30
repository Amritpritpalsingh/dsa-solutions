class Solution(object):
    def superPow(self, a, b):
      
        result = 1
        MOD = 1337
        for digit in b:
            result = pow(result, 10, MOD) * pow(a, digit, MOD) % MOD
        return result
        