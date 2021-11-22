for _ in range(int(input())):
    x=int(input())
    a=str(input())
    b=str(input())
    ans=0
    f=0
    f1=0
    flag=False
    for i in range(x-1,-1,-1):
        if a[i]<b[i]:
            ans+=1
            flag=True
        elif a[i]>b[i]:
            flag=False
        elif a[i]==b[i]:
            if flag:
                ans+=1
            continue
        #print(i,f,f1)

    print(ans)
