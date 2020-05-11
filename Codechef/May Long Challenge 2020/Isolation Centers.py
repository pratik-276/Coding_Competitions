t = int(input())

while t:
    n,q = map(int, input().split())
    s = input()
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    lst = list(d.values())
    while q:
        c = int(input())
        cq = 0
        for i in range(len(lst)):
            if lst[i]-c>0:
                cq += lst[i]-c
        print(cq)
        q-=1
    t-=1
