
cpdef list transpose(list matrix,int row,int column):
    cdef int arr[100][100]
    cdef list new_array=[]
    cdef int new2_array[100][100]
    for i in range(row):
        for j in range(column):
            arr[i][j]=matrix[i][j]
    for i in range(column):
        for j in range(row):
            new2_array[i][j]=arr[j][i]
    for i in range(column):
        new_array.append([new2_array[i][j] for j in range(row)])
    return new_array
