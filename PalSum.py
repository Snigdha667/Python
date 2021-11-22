def ok(num, arr): 
    for i in range(num-1,-1,-1): 
        if(arr[i]==1): 
            return i+1
            
arr = [0 for i in range(1000)] 
for i in range(1,1001): 
    st = str(bin(i)).replace("0b","") 
    if(st[::-1]==st): 
        arr[i-1]=1 
        
T = int(input())
for i in range(T): 
    N = int(input()) 
    ans=[] 
    while(N>0): 
        num = ok(N,arr) 
        ans.append(num) 
        N-=num
    print(len(ans))
    print(*ans, sep = " ")