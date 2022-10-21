from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    print(el)

i = 0
for el in cycle([1, 2, 3]):
    if i > 10:
        break
    print(el)
    i += 1
