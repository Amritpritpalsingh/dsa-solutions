class Solution(object):
    def transpose(self, mat):
        T = []
        for i in range(len(mat[0])):
            rows = []
            for j in range(len(mat)):
                rows.append(mat[j][i])
            T.append(rows)
        return T