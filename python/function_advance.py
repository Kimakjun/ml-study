import time
from pprint import pprint

data = [{'name': 'AA', 'price': 32.2, 'shares': 100},
        {'name': 'IBM', 'price': 91.1, 'shares': 50},
        {'name': 'CAT', 'price': 83.44, 'shares': 150},
        {'name': 'MSFT', 'price': 51.23, 'shares': 200},
        {'name': 'GE', 'price': 40.37, 'shares': 95},
        {'name': 'MSFT', 'price': 65.1, 'shares': 50},
        {'name': 'IBM', 'price': 70.44, 'shares': 100}]


def sub(a, b):
    print("Sub", a, b)
    return a - b


## 클로저
def add(x, y):
    def do_add():
        print("Adding", x, y)
        return x + y

    return do_add


def after(seconds, func):
    time.sleep(seconds)
    func()


def greeting():
    print('Hello Jun')


def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add2(x, y):
    return x + y

# 정적 메서드

# 클래스 메서드

if __name__ == '__main__':
    data.sort(key=lambda x: x['name'])
    pprint(data)

    # after(3, greeting)
    #
    # after(3, add(3, 5))

    log_sub =  logged(sub)
    log_sub(2, 3)

    result = add2(2, 4)
    print(result)