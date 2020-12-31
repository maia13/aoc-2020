import re

def n(input, sX, sY, wX, wY):
   return sX, sY, wX, wY+input

def e(input, sX, sY, wX, wY):
   return sX, sY, wX+input, wY

def w(input, sX, sY, wX, wY):
   return sX, sY, wX-input, wY

def s(input, sX, sY, wX, wY):
   return sX, sY, wX, wY-input

# w 10, 4; s 170, -38
# R90 | w 4, -10; s 170, -38
def r(input, sX, sY, wX, wY):
   wx, wy = rot(1, -1, wX, wY, int(input/90))
   return sX, sY, wx, wy

def l(input, sX, sY, wX, wY):
   wx, wy = rot(-1, 1, wX, wY, int(input/90))
   return sX, sY, wx, wy

def rot(patX, patY, x, y, times):
   rx, ry = x, y
   for _ in range(times):
      rx, ry = patX * ry, patY * rx
   return rx, ry

# w 4, -10; s 170, 38
# F11 | s + 11*4, -110 = 214, -72
def f(input, sX, sY, wX, wY):
   return sX + input*wX, sY + input*wY, wX, wY

# [1, 2] -> [2, -1] -> [-1, -2] -> [-2, 1]

inst_hash = { 'N': n, 'E': e, 'S': s, 'W': w, 'R': r, 'L': l, 'F': f}

def calculate(file_name):
   fo = open(file_name, "r+")
   rows = [parse_line(line.strip()) for line in fo.readlines()]

   sX, sY, wX, wY = 0, 0, 10, 1
   for inst, num in rows:
      sX, sY, wX, wY = inst_hash[inst](num, sX, sY, wX, wY)
   
   return abs(sX) + abs(sY)

def parse_line(line):
   inst = line[0]
   num = int(line[1:])
   return inst, num
