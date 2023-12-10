## 리스트 생성
a = [1, 2, 3, 4, 5]
b = [2 * x for x in a]
print(b)

names = ['Elwood', 'Jake']
a = [name.lower() for name in names]
print(a)

# 필터링
a = [1, -5, 4, 2, -2, 19]
b = [x for x in a if x > 0]
print(b)

# 의미하는바
'''
## [ <표현식> for <변수명> in <시퀀스> if <조건>]
result = []
for 변수 in 시퀀스:
    if 조건:
        result.append(표현식)
'''

# 용례
stokcs = [{'a': 100, 'b': 10}, {'a': 200, 'b': 10}, {'a': 300, 'b': 10}]
cost = sum([s['a'] for s in stokcs if s['a'] > 100])
print(cost)

# 유래
'''
조건 제시법이라는데.. 
'''
if __name__ == '__main__':
    pass
