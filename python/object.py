import copy

a = 4
b = 4

print(a is b)

## 깊은 복사
a = [2, 3, [100, 101], 4]
b = copy.deepcopy(a)

a[2].append(3)

print(a[2] is b[2])

# 타입 검사
a = []

if isinstance(a, (list, tuple)):
    print('a is a list or tuple')


if __name__ == '__main__':
    pass
