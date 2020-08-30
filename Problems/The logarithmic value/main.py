import math

positive = int(input())
base = int(input())

if base <= 1:
    print(round(math.log(positive), 2))
else:
    print(round(math.log(positive, base), 2))
