class Solution(object):
    def sumSubarrayMins(self, arr):
        mod = 10**9 + 7
        n = len(arr)

        # Previous Smaller Element (strictly smaller)
        pse = [-1] * n
        st = []
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            pse[i] = st[-1] if st else -1
            st.append(i)

        # Next Smaller Element (smaller or equal)
        nse = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            nse[i] = st[-1] if st else n
            st.append(i)

        # Calculate sum
        result = 0
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            result = (result + arr[i] * left * right) % mod

        return result
