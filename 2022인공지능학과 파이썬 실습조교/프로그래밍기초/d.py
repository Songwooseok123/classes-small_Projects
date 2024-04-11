#def get_integer(message,i,j):
#    digit = input(message)
#    while not (digit.isdigit() and i <= int(digit) <= j):
#        digit = input(message)
#    return int(digit)
#i = get_integer("Row#(1,2,3,4): ",1,4) - 1

#print(i)

while True:
    try:
        print('0이 아닌 정수를 입력해 주세요:', end=' ')
        user_number = int(input())
        print(1 / user_number)
        #break  # 예외가 발생하지 않은 경우, 반복을 빠져나간다
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('입력한 값은 정수가 아닙니다.')
