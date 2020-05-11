t = int(input())

while t:
    n = int(input())
    lst = list(map(int, input().split()))
    cst = []
    for i in range(n):
        c=1
        for j in range(i+1,n):
            if lst[j]-lst[j-1]>=3:
                break
            else:
                c+=1
        for j in range(i-1,-1,-1):
            if lst[j+1]-lst[j]>=3:
                break
            else:
                c+=1
        cst.append(c)
    print(min(cst), max(cst))
    t-=1
