t = int(input())

while t:
    n = int(input())
    lst = list(map(int,input().split()))
    sum = 0
    for i in range(n-1):
        sum += abs(lst[i+1]-lst[i])-1
    print(sum)
    t-=1
