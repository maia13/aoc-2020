import re

def calculate():
   fo = open("data.txt", "r+")
   lines = [line.strip() for line in fo.readlines()]

   w = len(lines[0])
   h = len(lines)

   total = 1
   total *= count_slope(lines, w, h, 1, 1)
   total *= count_slope(lines, w, h, 3, 1)
   total *= count_slope(lines, w, h, 5, 1)
   total *= count_slope(lines, w, h, 7, 1)
   total *= count_slope(lines, w, h, 1, 2)

   return total

def count_slope(lines, w, h, x_offset, y_offset):
   total = 0
   x, y = (0, 0)
   while y < h:
      if lines[y][x % w] == '#':
         total += 1

      x, y = (x + x_offset, y + y_offset)

   return total
