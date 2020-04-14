# cook your dish here

t = int(input())

while t:
    n = int(input())
    lst = list(map(int,input().split()))
    lst1 = []
    flag = 0
    for i in range(n):
        if lst[i] == 1:
            lst1.append(i)
    for j in range(len(lst1)-1):
        if lst1[j+1] - lst1[j] < 6:
            flag = 1
            print("NO")
            break
    if flag==0:
        print("YES")
    t-=1