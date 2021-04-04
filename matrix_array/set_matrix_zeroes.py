class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])
        set_r = set(())
        set_c = set(())
        
        for i in range(0,m):
            for j in range(0,n):
                
                if matrix[i][j]==0:
                    set_r.add(i)
                    set_c.add(j)
                 
                 
        for i in range(0,m):
            for j in range(0,n):
                if i in set_r or j in set_c:
                    matrix[i][j] = 0
                    
        return matrix
        