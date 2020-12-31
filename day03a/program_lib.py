import re

def calculate():
   fo = open("data.txt", "r+")
   lines = [line.strip() for line in fo.readlines()]

   w = len(lines[0])
   h = len(lines)

   total = 0
   x, y = (0, 0)
   while y < h:
      if lines[y][x % w] == '#':
         total += 1

      x, y = (x + 3, y + 1)

   return total

