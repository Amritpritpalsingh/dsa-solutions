from Queue import LifoQueue
class Solution(object):
    def isValid(self, s):
        if(len(s)==1 or len(s)==0):
            return False
        st = LifoQueue()
        for i in s:
            if i in "([{":
                st.put(i)
            else:
                if(st.qsize()==0):return False
                x = st.get()
                if((i==")" and x=="(") or (i=="]" and x=="[") or (i=="}" and x=="{")):
                    continue
                else:
                    return False

        return True
            

                
        