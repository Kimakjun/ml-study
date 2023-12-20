def f(x, *args, **kwargs):
    print(x)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    pass


if __name__ == '__main__':
    f(1, 2, 3, 4, 5, a="a", b="b")
    print("----")
    numbers = (2, 3, 4)
    options = {'a': '1', 'b': '2'}
    f(1, *numbers, **options)
