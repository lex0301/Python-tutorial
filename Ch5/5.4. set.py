# coding=UTF-8

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)


print("-" * 40)


a = set('abracadabra')
b = set('alacazam')
print(a)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)


print("-" * 40)


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
