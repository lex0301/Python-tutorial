# coding=UTF-8

def concat(*args, sep="/"):
    return sep.join(args)

a=concat("earth", "mars", "venus")
print(a)

b=concat("earth", "mars", "venus", sep=".")
print(b)
