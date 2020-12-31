import re
from collections import Counter

def calculate(file_name):
   fo = open(file_name, "r+")
   numbers = [int(line.strip()) for line in fo.readlines()]
   y = sorted(numbers)
   last = y[-1] + 3
   y.append(last)
   y = [0] + y
   z = zip(y[1:], y[0:-1])
   c = Counter([a-b for a, b in z])

   return c[1] * c[3]

