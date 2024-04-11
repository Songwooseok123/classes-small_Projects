### 실습 3.1 - 짝수 확인 함수 (p.100)
def even(n):
    return n % 2 == 0

print(even(13)) # False

# 실습  3-4.py
def smaller(x,y):
    if x < y:
        return x
    else:
        return y

# # Test code

print(smaller(3,5)) # returns 3
# print(smaller(5,3)) # returns 3
# print(smaller(3,3)) # returns 3

### 실습 3.5 - 셋 중 가장 작은 수 찾기 함수 (p.109)


def smallest(x,y,z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

# # Test code
# print(smallest(3,5,9)) # returns 3
# print(smallest(5,3,9)) # returns 3
# print(smallest(5,9,3)) # returns 3
### 실습 3.6 - 셋 중 가장 작은 수 찾기 함수 (smaller 활용) (p.110)

def smallest(x,y,z):
    return smaller(smaller(x,y),z)


### 실습 3.7 - 수강과목 평균 점수 계산 서비스 (p.115-117)

# # code : 3-13.py
# print("Score Average Calculator")
# number = int(input("How many classes? "))
# total = 0
# count = 0
# while count < number:
#     score = int(input("Enter your score: "))
#     total += score # total = total + score
#     count += 1 # count = count + 1
# print("Your average score =", end=' ')
# if count > 0:
#     print(round(total/number, 1))
# else:
#     print("0.0")
