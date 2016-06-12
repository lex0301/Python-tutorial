# coding=UTF-8

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
a = f(0)
print(a)
b = f(1)
print(b)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

pairs.sort(key=lambda pair: pair[0])
print(pairs)
