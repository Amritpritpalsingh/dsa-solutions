class Solution(object):
    def subArrayRanges(self, arr):
        n = len(arr)

        # ---------- MINIMUMS ----------
        pse = [-1] * n
        nse = [n] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            pse[i] = st[-1] if st else -1
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            nse[i] = st[-1] if st else n
            st.append(i)

        sum_min = 0
        for i in range(n):
            sum_min += arr[i] * (i - pse[i]) * (nse[i] - i)

        # ---------- MAXIMUMS ----------
        pge = [-1] * n
        nge = [n] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            pge[i] = st[-1] if st else -1
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            nge[i] = st[-1] if st else n
            st.append(i)

        sum_max = 0
        for i in range(n):
            sum_max += arr[i] * (i - pge[i]) * (nge[i] - i)

        return sum_max - sum_min
