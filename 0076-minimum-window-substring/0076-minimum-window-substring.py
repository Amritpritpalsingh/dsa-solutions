class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        from collections import Counter

        need = Counter(t)
        window = {}
        required = len(need)
        formed = 0

        l = 0
        ans = (float("inf"), None, None)

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
