def vowel_numbering(word):
    number = 1
    newword = ''
    for c in word:
        if c in ['a','e','i','o','u','A','E','I','O','U']:
            newword = newword + str(number) 
            number = number + 1
        else:
            newword = newword + c
    return newword

# # Test code
print(vowel_numbering('Massachussettes')) # 'M1ss2ch3ss4tt5s'



def drop_before(s,index):
    while s != [] and index > 0:
        s = s[1:]
        index -= 1
    return s

def take_before(s,index):
    ss = []
    while s != [] and index > 0:
        ss.append(s[0])
        s = s[1:]
        index -= 1
    return ss
def sublist(s,low,high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low <= high:
        return take_before(drop_before(s,low),high-low)
    else:
        return []

s = [1,2,3,4,5]
print(sublist(s,2,4)) # [3, 4]
