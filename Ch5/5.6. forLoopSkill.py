# coding=UTF-8

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

print("-" * 40)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

print("-" * 40)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}?  It is {1}.'.format(q, a))

print("-" * 40)

for i in reversed(range(1, 10, 2)):
	print(i)

print("-" * 40)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
	print(f)

print("-" * 40)

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)
print(words)
