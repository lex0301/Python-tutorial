# coding=UTF-8

def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here. 我是返回注释.":
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)

f('wonderful')
