import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    arr=map(float,arr)
    b=arr.reverse()
    a=numpy.array(arr)
    return a
    
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)