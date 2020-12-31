import re

def n(num, move_func = None):
   return 0, -num, 0

def e(num, move_func = None):
   return num, 0, 0

def w(num, move_func = None):
   return -num, 0, 0

def s(num, move_func = None):
   return 0, num, 0

def r(num, move_func = None):
   return 0, 0, int(num/90)

def l(num, move_func = None):
   return 0, 0, int(-num/90)

def f(num, move_func):
   return move_func(num)

inst_hash = { 'N': n, 'E': e, 'S': s, 'W': w, 'R': r, 'L': l, 'F': f}

# n, e, s, w
# 0, 90, 180, 270,
# 0, 1, 2, 3
directions = [n, e, s, w]

# 279 too low
def calculate(file_name):
   fo = open(file_name, "r+")
   rows = [parse_line(line.strip()) for line in fo.readlines()]
   d = 1 # east
   x, y = 0, 0
   for inst, num in rows:
      xoff, yoff, doff = inst_hash[inst](num, directions[d])
      x += xoff
      y += yoff
      d = (d + doff) % 4
      print(inst, num, '|', x, y, d)
   
   return abs(x) + abs(y)

def parse_line(line):
   inst = line[0]
   num = int(line[1:])
   return inst, num
