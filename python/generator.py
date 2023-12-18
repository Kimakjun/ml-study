# 이터레이션 내부 동작
import os
import re
import time

import follow as follow

x = [1, 2, 3]
it = x.__iter__()
print(it.__next__())


# 커스텀 이터레이터
class Test:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()


def countdown(n):
    # print 문을 추가했다
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1


def tail_file(file):
    file.seek(0, os.SEEK_END)  # 프로그램 다시 시작할시 이전것 안읽기 위해서 추가함
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        if line == 'exit':
            return
        yield line


def extract_numbers(lines):
    for line in lines:
        numbers = re.findall(r'\d+', line)
        for number in numbers:
            yield number


def print_numbers(numbers):
    for number in numbers:
        print(number)


def generator_pipeline():
    with open('../files/text.txt', 'r') as f:
        lines = tail_file(f)
        numbers = extract_numbers(lines)
        print_numbers(numbers)


def generator_expression():
    a = [1, 2, 3, 4]
    b = (2 * v for v in a) # 리스트컴프리헨션은 리스트 생성 x, 오로지 이터레이션, 소비되면 재사용 불가
    print(b)
    for v in b:
        print(v)

    # 아래 iterator 는 출력 x
    for v in b:
        print(v)


if __name__ == '__main__':
    generator_pipeline()
    generator_expression()


# 제너레이터 사용이유
"""
제너레이터를 사용하는 이유
많은 프로그램은 이터레이션으로 깔끔하게 표현된다.
항목들의 컬렉션을 루핑하며 몇 가지 연산(검색, 교체, 수정 등)을 수행한다.
파이프라인을 처리하는 것은 더 넓은 범위의 데이터 처리 문제가 적용된다.
메모리를 더 효율적으로 사용한다.
필요할 때만 값을 생산한다.
거대한 리스트를 생성하는 것과 대비된다.
스트리밍 데이터를 다룰 수 있다
제너레이터는 코드 재사용을 촉진한다
코드에서 이터레이션과 이터레이션 사용을 분리한다.
흥미로운 이터레이션 함수의 도구모음을 만들고 믹스 앤 매치할 수 있다.

itertools 모듈
itertools는 이터레이터/제너레이터를 돕도록 설계된 다양한 함수가 있는 라이브러리 모듈이다.

itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)

"""