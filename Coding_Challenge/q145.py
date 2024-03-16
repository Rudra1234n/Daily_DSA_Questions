def booleanMatrix(matrix):
   
    r = len(matrix)  
    c = len(matrix[0]) 

    R = [0] * r
    C = [0] * c

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                R[i] = 1
                C[j] = 1
    
    for i in range(r):
        for j in range(c):
            matrix[i][j] = R[i] or C[j]
