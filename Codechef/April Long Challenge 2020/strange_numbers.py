import math as mt
'''
the intution behind the problem is that the number of factors of tha numbers is
related to the power of primes . if a number can be expressed as n=a1^n1*a2^n2...
where a1 , a2 ... ar distinct primes then number of factors of n is (n1+1)*(n2+1)
so ultimately the problem breaks down to if x can be expressed as product of k numbers
or not.
'''


def solve(n, k): 
    a = [] 
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2
    for i in range(3, int(mt.ceil(mt.sqrt(n))), 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
            
    if n > 2: 
        a.append(n) 
          
    if len(a) < k: 
        return False
    else:
        return True
        

t=input()
while (t>0):

    n,k=map(int,raw_input().split())
    res=solve(n,k)
    if res:
        print(1)
    else:
        print(0)
    t-=1
