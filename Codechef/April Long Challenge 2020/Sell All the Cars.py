# cook your dish here

t = int(input())

while t:
    n = int(input())
    car = list(map(int,input().split()))
    sum = 0
    car.sort(reverse=True)
    for i in range(n):
        if (car[i] - i) > 0:
            car[i] = car[i] - i
        else:
            car[i] = 0
        sum += car[i]
    '''for i in range(n):
        sum += car[i]
        for j in range(i+1,n):
            if car[j] > 0:
                car[j] -= 1'''
    print(sum%1000000007)
    t-=1