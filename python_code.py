#f(n)=9*f(n-1) -11*f(n-2)
n=list(map(int,input().split()))
def is_part_of_series(list):
    a="Is part of series"
    b="Not part of series"
    m=[0,1]
    f=[]
    c=0
    for i in n:
        for j in range(2,i):
            m.append(9*m[j-1]-11*m[j-2])
        f.append(9*m[i-1]-11*m[i-2])
    for i in range(len(f)):
        if n[i]==f[i]:
            c+=1
    if c==len(f):
        print(a)
    else:
        print(b)
is_part_of_series(n)
