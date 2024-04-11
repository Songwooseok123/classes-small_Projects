### 실습 2.1 - 키보드 입력과 반올림 (p.66)
from math import pi
radius = float(input("Enter the radius: "))

area = pi * radius ** 2
print("The area of a circle with radius", radius, "is", round(area,1))

### 실습 2.2 - 동전 합산 서비스 (p.67)

print("Enter the number of coins you have.")
coin500 = int(input("500 won? "))
coin100 = int(input("100 won? "))
coin50 = int(input("50 won? "))
coin10 = int(input("10 won? "))
total = coin500 * 500 + coin100 * 100 + coin50 * 50 + coin10 * 10
print("You have", total, "won in total.")

### 실습 2.3 - 온도 변환 서비스 (p.72)

print("Fahrenheit to Celsius conversion")
f = int(input("Degrees in Fahrenheit? "))
c = (f - 32) * 5 / 9
print(round(c,1), "degrees in Celsius")


#### 2.2 함수

### 실습 2.4 - 동전 합산 함수 (p.83)

# code : 2-17.py
def coin_in_total(c500, c100, c50, c10):
    return c500 * 500 + c100 * 100 + c50 * 50 + c10 * 10

print("Enter the number of coins you have.")
coin500 = int(input("500 won? "))
coin100 = int(input("100 won? "))
coin50 = int(input("50 won? "))
coin10 = int(input("10 won? "))
total = coin_in_total(coin500, coin100, coin50, coin10)
print("You have", total, "won in total.") 

### 실습 2.5 - 온도 변환 함수 (p.84)

# code : 2-18.py
def fahrenheit2celsius(f):
    return (f - 32) * 5 / 9

print(fahrenheit2celsius(67)) # 19.444444444444443
print(round(fahrenheit2celsius(67),1)) # 19.4


### 실습 2.6 - 9의 보수 계산 함수 (p.85)

# code : 2-19.py
def complement_nine(n):
    return 10 ** len(str(n)) - 1 - n

# # Test code
print(complement_nine(0)) # 9 
print(complement_nine(9)) # 0 
print(complement_nine(4)) # 5 
print(complement_nine(18)) # 81 
print(complement_nine(40)) # 59 
print(complement_nine(307)) # 692 
print(complement_nine(9142)) # 857 
print(complement_nine(9965)) # 34 
print(complement_nine(9999)) # 0

