class Solution(object):
    def divide(self, dividend, divisor):
        flag = 0
        if divisor > 0 and dividend < 0:
            flag = 1
        if divisor < 0 and dividend >= 0:
            flag = 1

        dvsr = abs(divisor)
        dvdnt = abs(dividend)
        res = 0

        while dvdnt >= dvsr:
            cnt = 0
          
            while (dvsr << (cnt + 1)) <= dvdnt:
                cnt += 1
            res += 1 << cnt
            dvdnt -= dvsr << cnt

        
        if flag == 1 and res > 2**31:
            return -2**31
        if flag == 0 and res > 2**31 - 1:
            return 2**31 - 1

        if flag == 1:
            return -res
        else:
            return res
