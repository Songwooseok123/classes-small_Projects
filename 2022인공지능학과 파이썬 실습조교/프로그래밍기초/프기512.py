### 실습 7.1 - comb 함수의 실행 시간 측정 함수 (p.342)

# code : 7-7.py
def comb(n,r):
    if r != 0 and r != n:
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1

# # Test code
print(comb(30,3))  # 4060
# print(comb(30,27)) # 4060
# print(comb(30,7))  # 2035800
# print(comb(30,23)) # 2035800
# print(comb(30,10)) # 30045015 - 좀 오래 걸림
# print(comb(30,20)) # 30045015 - 좀 오래 걸림
# print(comb(30,15)) # 155117520 - 매우 오래 걸림

def run_comb(n,r):
    from time import perf_counter
    start = perf_counter()
    answer = comb(n,r)
    finish = perf_counter()
    print("comb(", n, ",", r, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")

# # Test code
#run_comb(30,3)  # 4060 - 0.001 seconds
# run_comb(30,27) # 4060 - 0.0011 seconds
# run_comb(30,7)  # 2035800 - 0.5204 seconds
# run_comb(30,23) # 2035800 - 0.5472 seconds
# run_comb(30,10) # 30045015 - 7.8143 seconds
# run_comb(30,20) # 30045015 - 7.9519 seconds
#run_comb(30,15) # 155117520 - 41.1853 seconds

### 실습 7.2 - comb_pascal 함수의 실행 시간 측정 (p.349)

# code : 7-8.py
def comb_pascal(n, r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] + [[1] for _ in range(n-r)]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]

def run_comb_pascal(n,r):
    from time import perf_counter
    start = perf_counter()
    answer = comb_pascal(n,r)
    finish = perf_counter()
    print("comb_pascal(", n, ",", r, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")

# # Test code
#run_comb_pascal(30,3)  # 4060 - 0.0 seconds
# run_comb_pascal(30,27) # 4060 - 0.0 seconds
# run_comb_pascal(30,7)  # 2035800 - 0.0001 seconds
# run_comb_pascal(30,23) # 2035800 - 0.0 seconds
# run_comb_pascal(30,10) # 30045015 - 0.0001 seconds
# run_comb_pascal(30,20) # 30045015 - 0.0001 seconds
run_comb_pascal(30,15) # 155117520 - 0.0001 seconds


#### 7.3 1까지 줄이는 최소 스텝

### 실습 7.3 - 표채워풀기 알고리즘 구현 (p.357)

# code : 7-13.py
def minsteps(n):
    memo = [0 for _ in range(n+1)]
    print("memo = ", memo) 
    for i in range(2,n+1):
        print(i)
        steps = memo[i-1]
        print("steps =", steps)
        if i % 2 == 0:
            steps = min(steps, memo[i//2])
        if i % 3 == 0:
            steps = min(steps, memo[i//3])
        print("바뀐 steps=",steps)
        memo[i] = steps + 1
        print("for문 한 번 돌고 바뀐 memo",memo)
    return memo[n]

def run_minsteps(n):
    from time import perf_counter
    start = perf_counter()
    answer = minsteps(n)
    finish = perf_counter()
    print("minsteps(", n, ") => ", answer, sep="")
    print(round(finish-start), "seconds")

# # Test code
#print(run_minsteps(3))       # 1
# print(run_minsteps(4))       # 2
print(run_minsteps(7))       # 3
# print(run_minsteps(10))      # 3
# print(run_minsteps(23))      # 6
# print(run_minsteps(237))     # 8
# print(run_minsteps(317))     # 10
# print(run_minsteps(514))     # 8
# print(run_minsteps(711))     # 9
# print(run_minsteps(908))     # 11
# print(run_minsteps(1000))    # 9
# print(run_minsteps(2020))    # 10
# print(run_minsteps(1111111)) # 19

#### 7.4 하노이의 탑

### 실습 7.4 - tower_of_hanoi 함수의 실행 시간 예측 (p.362)

# 28개 = 약 1분
# 29개 = 약 2분
# 30개 = 약 4분
# 31개 = 약 8분
# 32개 = 약 16분
# 33개 = 약 32분
# 34개 = 약 64분 = 1시간 4분
# 35개 = 약 128분 = 2시간 8분
# 36개 = 약 256분 = 4시간 16분
# 37개 = 약 512분 = 8시간 32분
# 38개 = 약 1024분 = 17시간 4분
# 39개 = 약 2048분 = 34시간 8분
'''
def tower_of_hanoi(n, source, dest, temp):
    global count # 전역 변수 (global variable)
    if n > 1:
        tower_of_hanoi(n-1, source, temp, dest)
        count += 1
        tower_of_hanoi(n-1, temp, dest, source)
    else:
        count += 1
for n in [4,6,8,16,24,25,26,27,28]:
    count = 0
    from time import perf_counter
    start = perf_counter()
    tower_of_hanoi(n, "A", "C", "B")
    finish = perf_counter()
    print("원반", n, "개 :", count, "번 이동,", round(finish-start, 1), "초")

'''
'''
def digit_art_horizontal_left_down(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1, end=' ')
        print()

# # Test code
digit_art_horizontal_left_down(7)

def digit_art_horizontal_left_up(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()
'''
### 실습 8.2

def digit_art_vertical_right_down(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(' ', end=' ')
        for _ in range(i):
            print(i,end=' ') 
        print()

# # Test code
digit_art_vertical_right_down(7)
def digit_art_vertical_right_down(n):
    for i in range(1,n+1):
        for _ in range(i-1):
            print(' ', end=' ')
        for _ in range(n-i+1):
            print(i,end=' ') 
        print()
digit_art_vertical_right_down(7)

### 실습 8.3
def digit_art_vertical_alternate(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end=' ')
            else:
                print(n-i, end=' ')
        print()
print("ddddd")
digit_art_vertical_alternate(7)        
print("ddddd")
###실습 8.4

def bubble(ns):
    for k in range(len(ns)-1,0,-1):
        for i in range(k):
            if ns[i] >ns[i+1]:
                ns[i],ns[i+1] = ns[i+1] ,ns[i]
    return ns
print(bubble([32,23,18,7,11,99,55]))
### 실습 8.5
'''
def radixsort(ds):
    if ds != []:
        length = len(ds[0])
        for i in range(length-1,-1,-1):
            print(i)
            distributed = [[] for _ in range(10)]
            for d in ds:
                print(d)
                distributed[int(d[i])].append(d)
                print(distributed)
            ds = []
            for d in distributed:
                print(ds)
                ds += d
            print(ds)    
            #print(ds)
        return ds
    else:
        return []

# # Test code
#print(radixsort([]))
#print(radixsort(["239"]))
print(radixsort(["170",'045','075','090','002','024','802','066']))
#print(radixsort(["239",'234','879','878','123','358','416','317','137','225']))
#print(radixsort(["0505", "0515", "1225", "0915", "1111", "0101", "0318", "0301"]))
print(radixsort(["01000", "00100", "00001", "10000", "00010"]))
'''
###실습 8.6
import random
def initialize_board_4x4():
    row0 = [1,2,3,4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]
def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom
def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

# # Test code
b1=initialize_board_4x4()
for b in b1 :
    print(b)
print("")
trans_b1 = transpose(b1)
for b in trans_b1 :
    print(b)
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1        
    return board
print(make_holes(b1, 4))
