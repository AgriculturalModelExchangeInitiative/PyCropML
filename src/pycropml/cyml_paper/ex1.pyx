def sum_(int x[]):
    cdef int i, y=0
    for i in x:
        y = y + i
    return y