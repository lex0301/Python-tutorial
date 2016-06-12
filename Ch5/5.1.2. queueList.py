# coding=UTF-8

from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry")
queue.append("Graham")
print(queue)

a = queue.popleft()
print(a)

b = queue.popleft()
print(b)

print(queue)
