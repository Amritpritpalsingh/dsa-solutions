from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Push element into q2
        self.q2.append(x)
        # Move all elements from q1 → q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap q1 and q2 so q1 has newest element at front
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0
