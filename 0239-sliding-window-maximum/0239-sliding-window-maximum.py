class Solution(object):
    from collections import deque

    def maxSlidingWindow(self, arr, k):
            n = len(arr)
            dq = deque()   # stores indices
            ans = []

            for i in range(n):
                # Remove indices out of window
                if dq and dq[0] <= i - k:
                    dq.popleft()

                # Maintain decreasing order
                while dq and arr[dq[-1]] <= arr[i]:
                    dq.pop()

                dq.append(i)

                # Add max to answer
                if i >= k - 1:
                    ans.append(arr[dq[0]])

            return ans
