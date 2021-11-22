t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    x1 = max(x)
    x2 = min(x)
    s = x1 - x2
    print(s)
