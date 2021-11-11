# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
s=list(map(int,raw_input().split()))
s1=[]
for i in range(s[0]):
    s1.append(list(map(int,raw_input().split())))
arr = numpy.array(s1)
print numpy.transpose(arr)
print arr.flatten()

