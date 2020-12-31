import re


def calculate(file_name):
   fo = open(file_name, "r+")
   lines = [line.strip() for line in fo.readlines()]
   width = len(lines[0])
   height = len(lines)

   changed = True
   while changed:
      changed, lines = turn(lines, width, height)

   return count_occupied(lines)

def pp(lines):
   for line in lines:
      print(''.join(line))
   print('')

def nw(x, y):
   return x-1, y-1

def n(x, y):
   return x, y-1

def ne(x, y):
   return x+1, y-1

def w(x, y):
   return x-1, y

def e(x, y):
   return x+1, y

def sw(x, y):
   return x-1, y+1

def s(x, y):
   return x, y+1

def se(x, y):
   return x+1, y+1

def count_occupied_around(lines, x, y, width, height):
   neighbour_pos = [
      (nw, x, y), (n, x, y), (ne, x, y),
      (w, x, y), (e, x, y),
      (sw, x, y), (s, x, y), (se, x, y)
      ]
   # print('....')
   occupied = 0
   while len(neighbour_pos) > 0:
      direction, xx, yy = neighbour_pos[0]
      neighbour_pos = neighbour_pos[1:]
      a, b = direction(xx, yy)
      if a >= 0 and b >= 0 and a < width and b < height:
         if lines[y][x] == '#':
            occupied += 1
         elif lines[y][x] == '.':
            neighbour_pos.append((direction, a, b))
      # print(len(neighbour_pos), xx, yy)

   # print('')
   
   return occupied

def turn(lines, width, height):
   changed = False
   new_lines = [None] * height
   for y in range(height):
      new_line = list(lines[y])
      new_lines[y] = new_line

      for x in range(width):
         occ = count_occupied_around(lines, x, y, width, height)
         seat = lines[y][x]
         if is_empty(seat) and occ == 0:
            new_line[x] = '#'
            changed = True
         elif is_occupied(seat) and occ >= 4:
            new_line[x] = 'L'
            changed = True

   return changed, new_lines

def is_empty(seat):
   return seat == 'L'

def is_occupied(seat):
   return seat == '#'

def count_occupied(lines):
   return len([True for line in lines for seat in line if is_occupied(seat)])