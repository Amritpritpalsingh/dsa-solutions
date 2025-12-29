class Solution(object):
    def largestRectangleArea(self, h):
        st = []
        area = 0
        el = 0
        for i in range(len(h)):
            while(len(st) and h[st[-1]]>h[i]):
                el = st.pop()
                nse = i
                pse = st[-1] if st else -1
                area = max(area,(h[el]*(nse-pse-1)))
            st.append(i)
        while(len(st)):
            el = st.pop()
            nse = len(h)
            pse = st[-1] if st else -1
            area = max(area,(h[el]*(nse-pse-1)))
        return area



        