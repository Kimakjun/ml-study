from collections import defaultdict, deque, Counter

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# Counter
# 초기값이 없어도 알아서 계산해줌
counter = Counter()
print(counter)
print(type(counter))
for name, shares, price in portfolio:
    counter[name] += shares
print(counter)

# 일대다 매핑
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
# defaultdict(<class 'list'>, {'GOOG': [(100, 490.1), (75, 572.45)], 'IBM': [(50, 91.1), (100, 45.23)], 'CAT': [(150, 83.44)], 'AA': [(50, 23.15)]})
print(holdings)

# deque
history = deque(maxlen=10)
for i in range(100):
    history.append(i)

print(history.pop())
print(history.pop())
print(history.pop())
print(history)

if __name__ == '__main__':
    pass
