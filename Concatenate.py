# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
s=list(map(int,raw_input().split()))
s1=[]
s2=[]
for i in range(s[0]):
    s1.append(list(map(int,raw_input().split())))
for j in range(s[1]):
    s2.append(list(map(int,raw_input().split())))
arr1 = numpy.array(s1)
arr2 = numpy.array(s2)
print numpy.concatenate((arr1, arr2), axis = 0)
