n=int(input())
for i in range(n,0,-1):
    print(' '*(i-1)+"H"*((n-i)*2+1))
for j in range(n+1):
    print(' '*(n-((n+1)/2))+"H"*n+' '*(5*n-2*n)+"H"*n)
for i in range((n+1)/2):
    print(' '*(n-((n+1)/2))+"H"*n*5)
for j in range(n+1):
    print(' '*(n-((n+1)/2))+"H"*n+' '*(5*n-2*n)+"H"*n)
for i in range(1,n+1):
    print(' '*(5*n-n)+' '*(i-1)+((n-i)*2+1)*"H")