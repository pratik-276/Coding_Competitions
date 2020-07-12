def calculate_power(a):
    if a<10:
        return a
    else:
        sum = 0
        while a>0:
            p = a%10
            sum += p
            a = a//10
        return sum

t = int(input())

while t:
    n = int(input())
    a_point = 0
    b_point = 0
    for i in range(n):
        lst = list(map(int,input().split()))
        a = calculate_power(lst[0])
        b = calculate_power(lst[1])
        if a>b:
            a_point += 1
        elif b>a:
            b_point += 1
        else:
            a_point += 1
            b_point += 1
    if a_point>b_point:
        print(0, a_point)
    elif a_point<b_point:
        print(1, b_point)
    else:
        print(2, b_point)
    t-=1
