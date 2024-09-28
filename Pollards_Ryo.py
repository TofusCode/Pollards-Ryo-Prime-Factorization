from math import gcd

#밀러-라빈 판정
def miller_rabin(n, a):
    d = n - 1 #홀수
    while d % 2 == 0:
        d = d >> 1 #2^d*r+1
    x = pow(a, d, n) #a^{d} % n 계산

    if x == 1 or x == n-1: #x가 1 또는 n-1이면 소수
        return True
    
    while d != n-1: #n-1이 아닌 동안 
        x = pow(x,2,n) #x^{2} % n 계산
        d *= 2

        #x가 1이면 합성수이고 아니면 소수
        if x == 1:
          return False
        if x == n-1:
          return True 
    
    return False

base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
def isPrime(n):
    if n in base:
        return True
    if n == 1 or n%2 == 0:
        return False
    
    for a in base: #n < 1,373,653의 수에 대해서는 a = 2, 3만 검사해도 충분함, n < 2^64에 대해서 37까지의 소수만 확인해도 됨
        #밀러-라빈이 성립하면 소수
        #성립하지 않아 false를 반환하면 소수가 아님 (not False = True)
        if not miller_rabin(n,a): 
            return False
    return True

def g(x,n):
    return ((x*x) + 1) % n

def pollard_ryo(n, x):
    p = x
    if isPrime(n):
        return n
    else:
        for i in base:
            if n % i == 0:
                return i
        y = x
        d = 1
        while d == 1:
            x = g(x,n)
            y = g(g(y,n),n)
            d = gcd(abs(x-y),n)
        if d == n:
            return pollard_ryo(n, p+1)
        else:
            if isPrime(d):
                return d
            else:
                return pollard_ryo(d,2)

n = int(input())
res = []
while n != 1:
    k = pollard_ryo(n,2)
    res.append(int(k))
    n = n // k

res.sort()
for i in res:
    print(i)