###########실습 4.1##############

'''
재귀함수로 구현한 코드 (4.10.py) 
def sumrange(m,n):
    if m <= n:
        return m + sumrange(m+1, n)
    else:
        return 0      

# 꼬리 재귀함수(4-11.py)
def sumrange(m,n):
    def loop(m,total):
        if m <= n:
            print("fd",m,n,total)
            return loop(m+1,total+m)
        else:
            print("f",m,n,total)
            return total
                
    return loop(m,0)
'''
'''
# while 루프 버전 code : 4-12.py
def sumrange(m,n):
    sum = 0
    while m <= n:
        sum = sum + m
        m = m + 1
    return sum
print(sumrange(3,4))
print(sumrange(1,4))

'''

###########실습 4.2##############
'''
def gcd(m,n):
    while n !=0:
        m,n=n,m%n
        
    return m

print(gcd(48,18))  # 6
print(gcd(18,48))  # 6
print(gcd(192,72)) # 24
print(gcd(18,57))  # 3
print(gcd(0,11))
'''
 
###########실습 4.3##############
'''
# 재귀함수 4.23
def even(x):
    return True if x%2==0 else False
def odd(x):
    return True if x%2==1 else False

def gcd(m,n):
    if not (m == 0 or n == 0): # 둘다 0이 아닐 때 
        if even(m) and even(n):
            return 2 * gcd(m//2,n//2)
        elif even(m) and odd(n):
            return gcd(m//2,n)
        elif odd(m) and even(n):
            return gcd(m,n//2)
        elif m <= n:
            return gcd(m,(n-m)//2)
        else:
            return gcd(n,(m-n)//2)
    else: # 둘 중 하나만 0이거나 둘다 0일 때 . 
        if m == 0:
            return n
        else:
            return m
print(gcd(48,18))  # 6
print(gcd(18,48))  # 6
print(gcd(192,72)) # 24
print(gcd(18,57))  # 3
print(gcd(0,11))            
print("ddd")
'''

# 꼬리재귀함수  4.24
def gcd(m,n):
    def loop(m,n,k):
        if not (m == 0 or n == 0):
            if m % 2 == 0 and n % 2 == 0:
                return loop(m//2,n//2,2*k)
            elif m % 2 == 0 and n % 2 == 1:
                return loop(m//2,n,k)
            elif m % 2 == 1 and n % 2 == 0:
                return loop(m,n//2,k)
            elif m <= n:
                return loop(m,(n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return n*k
            else: # n == 0
                return m*k
    return loop(m,n,1)

# # Test code
print(gcd(48,18))   # 6
print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0

