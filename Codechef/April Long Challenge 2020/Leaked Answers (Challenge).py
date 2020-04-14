# cook your dish here

t = int(input())

while t:
    n,m,k = map(int,input().split())
    for i in range(n):
        lst = list(map(int,input().split()))
        print(lst[0],end=' ')
    print('')
    t-=1