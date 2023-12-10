# 함수의작동

def divide(a, b):
    q = a // b
    r = a % b
    return q, r

x, y  = divide(3, 2)

print(x, y)