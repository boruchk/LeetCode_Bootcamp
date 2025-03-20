class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rowlen = len(matrix)
        collen = len(matrix[0])
        rowlist = []
        collist = []

        # find the index of the columns and rows that have a zero in them
        for row in range(rowlen):
            for col in range(collen):
                if matrix[row][col] == 0:
                    rowlist.append(row)
                    collist.append(col)

        # each column and row that has a 0: make it full of 0s
        for row in rowlist:
            matrix[row] = [0] * collen
        for col in collist:
            for row in range(rowlen):
                matrix[row][col] = 0