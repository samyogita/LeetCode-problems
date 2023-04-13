class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        st = []
        for ele in pushed:
            st.append(ele)
            while st and st[-1] == popped[i]:
                st.pop()
                i += 1
        return not st
