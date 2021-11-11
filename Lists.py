if __name__ == '__main__':
    n=int(raw_input())
s=[]
a=[]
for i in range(n):
    s.append(list(raw_input().split()))
for i in range(n):
    if s[i][0]=="insert":
        a.insert(int(s[i][1]),int(s[i][2]))
    elif s[i][0]=="print":
        print(a)
    elif s[i][0]=="remove":
        a.remove(int(s[i][1]))
    elif s[i][0]=="append":
        a.append(int(s[i][1]))
    elif s[i][0]=="sort":
        a.sort()
    elif s[i][0]=="pop":
        a.pop()
    elif s[i][0]=="reverse":
        a.reverse()
