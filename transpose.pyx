import array
def matrix_converter(matrix):
    cdef **arr
    cdef int n=0
    for i in matrix:
        *(*(arr+n))=matrix[n]
        n++
cpdef long long transpose()