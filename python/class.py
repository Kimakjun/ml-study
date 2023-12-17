# 프라이빗 어트리뷰트, 프로퍼티, 슬롯 등을 사용하지 마라.
# 이런 것들은 특수한 목적이 있으며,
# 다른 파이썬 코드를 읽다보면 눈에 띌 수 있다.
# 하지만 일상적인 코딩에는 거의 필요 없다.
class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        # setter 를 호출함.
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

class Loud:
    def noise(self):
        return super().noise().upper()


class Bike:
    def noise(self):
        return 'Bike'


class Dog:
    def noise(self):
        return 'Bark'


class LoudBike(Loud, Bike):
    pass


class LoudDog(Loud, Dog):
    pass




if __name__ == '__main__':
    # mixin
    lb = LoudBike()
    print(lb.noise())

    ld = LoudDog()
    print(ld.noise())

    # 캡슐화
    s = Stock('BM', 40, 91.1)
    print(s.shares)
    # s.shares = 'w'

    s.name = 'name'
    s.b = 'set'