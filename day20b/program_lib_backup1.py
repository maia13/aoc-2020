import re
from collections import Counter, defaultdict

def calculate(file_name):
   fo = open(file_name, "r+")
   square_size = 10
   lines = [line.strip() for line in fo.readlines()]
   total = 0
   # idx: [square, sides' options]
   sides_squares = defaultdict(list)
   squares = group_lines(lines, square_size)
   for idx in squares:
      square = squares[idx][0]
      sidesoptions = square_sides(square)
      for so, sidesoption in sidesoptions.items():
         for side in sidesoption:
            sides_squares[side].append((idx, so))
      squares[idx].append(sidesoptions)
      print(idx, squares[idx][1])
   pph(sides_squares)
   return -1

def pph(hash):
   print('------')
   for ix, val in hash.items():
      print(ix, val)

def group_lines(lines, square_size):
   squares = {}
   square = None
   for i, line in enumerate(lines):
      if i % (square_size+2) == 0:
         matched = re.match(r'^Tile (\d+):$', line)
         idx = int(matched[1])
         square = []
         squares[idx] = [square]
         continue
      if line:
         square.append(''.join(['1' if x == '#' else '0' for x in line]))
      
   return squares

# 123
# 456
# 789
#
# A) 123, 369, 789, 147
# B) 789, 963, 123, 741
# C) 321, 147, 987, 369
# D) 963, 321, 741, 987
# + rotation
# + reverse
def square_sides(square):
   top = square[0]
   right = [row[-1] for row in square]
   bottom = square[-1]
   left = [row[0] for row in square]

   result = {
      'a': [binint(top), binint(right), binint(bottom), binint(left)], # A)
      'b': [binint(bottom), rbinint(right), binint(top), rbinint(left)], # B)
      'c': [rbinint(top), binint(left), rbinint(bottom), binint(right)], # C)
      'd': [rbinint(right), rbinint(top), rbinint(left), rbinint(bottom)]  # D)
   }
   return result

   # return { binint(top),
   #          rbinint(top),
   #          binint(right),
   #          rbinint(right),
   #          binint(bottom),
   #          rbinint(bottom),
   #          binint(left),
   #          rbinint(left) }

def binint(s):
   if type(s) is list:
      return int(''.join(s), base=2)
   return int(s, base=2)

def rbinint(s):
   if type(s) is list:
      return int(''.join(s), base=2)
   return int(s[::-1], base=2)