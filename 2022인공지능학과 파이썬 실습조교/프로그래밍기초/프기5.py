'''
####################### 실습 4.9
###### 덧셈/뺄셈/반나누기 알고리즘 : while 루프 버전  
def fastmult(m,n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            m, n = m + m, n // 2
        else:
            n, ans = n - 1, m + ans
    return ans
print(fastmult(8,10))

####################### 실습 4.10
###### 러시아 농부  재귀함수 
def russian_mult(m,n):
    def loop(m,n):
        if n > 1:
            if n % 2 ==1 :
                return m + loop(2*m,n//2)
            
            else :
                return loop(2*m,n//2)
            
        else: # n == 1
            return m
        
    if n > 0:
        return loop(m,n)
    else:
        return 0


####################### 실습 4.11
###### 러시아 농부  꼬리재귀함수  
def russian_mult(m,n):
    def loop(m,n,a):
        if n > 1:
            if n % 2 == 1:
                return loop(m+m,n//2,a+m)
            else:
                return loop(m+m,n//2,a)
        else: # n == 0
            return a+m
    if n > 0:
        return loop(m,n,0)
    else:
        return 0
####################### 실습 4.12
###### 러시아 농부 while 루프  
def russian_mult(m,n):
    if n > 0:
        a = 0
        while n > 1:
            if n % 2 == 1:
                a = a + m
            m = m + m
            n = n // 2
        return a+m
    else:
        return 0
print(russian_mult(57,86))

####################### 연습  4.2
###### 팩토리얼 재귀  
def fac(n):
    if n > 1:
        return fac(n-1) * n
    else:
        return 1
#print(fac(4))
    
###### 팩토리얼 꼬리재귀
def fac(n):
    def loop(n,p):
        if n > 1:
            return loop(n-1,p*n)
        else:
            return p
    return loop(n,1)

###### 팩토리얼 while
def fac(n):
    ans =1
    while n>1:
        ans = ans *n
        n= n-1
    return ans
print(fac(4))

####################### 연습  4.3
###### 삼각수  재귀
def trunum(n):
    if n>=1 :
        return n+trunum(n-1)
    else :
        return 0
###### 삼각수  꼬리재귀
def trunum(n):
    def loop(n,r) : 
        if n>=1 :
            return loop(n-1,n+r)
        else :
            return r
    return loop(n,0)

###### 삼각수  while

def trunum(n):
    ans = 0
    while n>=1:
        ans = ans +n
        n = n-1
    return ans 
           
print(trunum(10))

####################### 실습 5.1
###### count timer while문 
from time import sleep
def countdown(n):
    while n > 0:
        print(n)
        sleep(1) # 1초간 정지 
        n = n-1
    print("LAUNCH")

###### count timer for문 
from time import sleep
def countdown(n):
    for i in range(n,0 ,-1 ):
        print(i)
        sleep(1) # 1초간 정지 
    print("LAUNCH")
countdown(10)

###### 자연수 수열의 합 while문 
def sigma(n):
    sum = 0
    while n>0:
        n,sum = n-1 , n+sum
    return sum

###### 자연수 수열의 합 for문 
def sigma(n):
    sum = 0
    for i in range(n,0,-1):
    	sum = sum + i
    return sum
print(sigma(10))

###### 구간  수열의 합 for문
def sumrange(m,n):
    sum = 0
    for i in range(m,n+1):
    	sum = sum + i

    return sum

###### 팩토리얼 for문
def fac(n):
    ans = 1
    for k in range(n,1,-1):
        ans = k * ans
    return ans
print(fac(4))
###### 거듭제곱 while문
def power(b,n):
    prod = 1
    while n>0:
    	prod = b*prod
    	n = n-1 
    return prod
###### 거듭제곱 for문
def power(b,n):
    prod = 1
    for i in range(n,0,-1):
    	prod = prod * b
    return prod


print(power(2,5))
'''
'''
####################### 실습 5.2 insert 재귀
def insert(x,ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return [ss[0]] + insert(x,ss[1:])
    else:
        return [x]
'''
'''
####################### 실습 5.3 insert 꼬리재귀
def insert(x,ss): 
    def loop(ss,left):
        if ss != []:
            if x <= ss[0]:
                left.append(x)
                return left+ss
            else:
                left.append(ss[0])
                return loop(ss[1:],left)
        else:
            left.append(x)
            return left
    return loop(ss,[])

####################### 실습 5.4 insert while문
'''
def insert(x,ss):
    ppp = []
    while ss != []:
        if x <= ss[0]:

            ppp.append(x)
            return ppp+ss 
        else:
            ppp.append(ss[0])
            ss = ss[1:]
    ppp.append(x)
    return ppp

#print(insert(3,[2,4,5,7,8])) # [2, 4, 5, 6, 7, 8]

####################### 실습 5.5 insertion_sort 꼬리재귀함수

def insertion_sort(xs):
    def loop(xs,ss):
        if xs != []:
            return loop(xs[1:],insert(xs[0],ss))
        else:
            return ss
    return loop(xs,[])


####################### 실습 5.6 insertion_sort while문

def insertion_sort(xs) :
    ss = []
    while xs != []:
        xs, ss = xs[1:], insert(xs[0],ss)
    return ss
####################### 실습 5.7 insertion_sort for문
def insertion_sort(xs) :
    ss = []
    for i in xs:
        ss =  insert(i,ss)
    return ss
#print(insertion_sort([3,5,4,2])) # [2, 3, 4, 5]


####################### 실습 5.8 merge 꼬리재귀함수

# 코드 5-25 :
def merge(left,right):
    if not (left == [] or right == []):
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:],right)
        else:
            return [right[0]] + merge(left,right[1:])
    else:
        return left + right
## 꼬리재귀
def merge(left,right):
    def loop(left,right,ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:],right,ss)
            else:
                ss.append(right[0])
                return loop(left,right[1:],ss)
        else:
            return ss + left + right
    return loop(left,right,[])

####################### 실습 5.9 merge while
def merge(left,right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left = left[1:]
        else:
            ss.append(right[0])
            right = right[1:]
    return ss + left + right
#print(merge([18,23,32],[7,11,55,99]))
####################### 실습 5.10 partition 꼬리재귀함수
# 5.29
def partition(pivot,xs):
    if xs != []:
        left, right = partition(pivot,xs[1:])
        
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        return left, right
    else:
        return [], []
## 꼬리재귀함수    
def partition(pivot,xs):
    def loop(xs,ls,rs):
        if xs != []:
            if xs[0] <= pivot:
                ls.append(xs[0])
            else:
                rs.append(xs[0])
            return loop(xs[1:],ls,rs)
        else:
            return ls, rs
    return loop(xs,[],[])

####################### 실습 5.11 partition while문
def partition(pivot,xs):
    ls, rs = [], []
    while xs != []:
        if xs[0] <= pivot:
            ls.append(xs[0])
        else:
            rs.append(xs[0])
        xs = xs[1:]
    return ls, rs
####################### 실습 5.11 partition for문
def partition(pivot,xs):
    ls, rs = [], []
    for i in  xs:
        if i <= pivot:
            ls.append(i)
        else:
            rs.append(i)
    return ls, rs

print(partition(12,[7,11,55,99]))
