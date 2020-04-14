# cook your dish here
t = int(input())

while t:
    n = int(input())
    if n==1:
        print('1')
        print('1 1')
    else:
        count = n//2
        print(count)
        if count == 1:
            if n==2:
                print('2 1 2')
            elif n==3:
                print('3 1 2 3')
        else:
            print('3 1 2 5')
            print('2 3 4')
            for i in range(6,n+1,2):
                if i==n:
                    print('1 {}'.format(i))
                else:
                    print('2 {} {}'.format(i,i+1))
    t-=1