if __name__ == '__main__':
    n = int(raw_input())
    arr =list(map(int,raw_input().split()))
    a=[]
    for i in arr:
        a.append(i)
        if i==max(arr):
            a.remove(i)
    print(max(a))
