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

def ppp(lines):
   for line in lines:
      print('|'.join([str(x) for x in line]))
   print('')

def e(x, y):
   return x+1, y

def sw(x, y):
   return x-1, y+1

def s(x, y):
   return x, y+1

def se(x, y):
   return x+1, y+1

def set_seat_count(seat):
   if seat == '.':
      return ' '
   else:
      return 0

def neighbour_counts(lines, width, height):
   matrix = [[set_seat_count(seat) for seat in line] for line in lines]

   # s
   for x in range(width):
      neighbour_counts_direction(lines, width, height, matrix, x, 0, s)
   # e
   for y in range(height):
      neighbour_counts_direction(lines, width, height, matrix, 0, y, e)
   # se
   for x in range(1, width):
      neighbour_counts_direction(lines, width, height, matrix, x, 0, se)
   for y in range(height):
      neighbour_counts_direction(lines, width, height, matrix, 0, y, se)
   # sw
   for x in range(width-1):
      neighbour_counts_direction(lines, width, height, matrix, x, 0, sw)
   for y in range(height):
      neighbour_counts_direction(lines, width, height, matrix, width-1, y, sw)
   return matrix

def neighbour_counts_direction(lines, width, height, matrix, startX, startY, direction):
   x, y = startX, startY
   prevX, prevY = -1, -1
   if lines[y][x] != '.':
      prevX, prevY = x, y

   while True: 
      x, y = direction(x, y)
      if not (x >= 0 and y >= 0 and x < width and y < height):
         return
      
      seat = lines[y][x]
      if seat == '.':
         continue
      if seat == '#':
         if prevX != -1:
            matrix[prevY][prevX] += 1
            if lines[prevY][prevX] == '#':
               matrix[y][x] += 1
         prevX, prevY = x, y
      if seat == 'L':
         if prevX != -1:
            if lines[prevY][prevX] == '#':
               matrix[y][x] += 1
         prevX, prevY = x, y

   raise Exception('It should not get here')


def turn(lines, width, height):
   changed = False
   new_lines = [None] * height
   matrix = neighbour_counts(lines, width, height)
   # pp(lines)
   # ppp(matrix)
   # print('-----')
   for y in range(height):
      new_line = list(lines[y])
      new_lines[y] = new_line

      for x in range(width):
         seat = lines[y][x]
         if seat == '.':
            continue
         occ = matrix[y][x]
         if is_empty(seat) and occ == 0:
            new_line[x] = '#'
            changed = True
         elif is_occupied(seat) and occ >= 5:
            new_line[x] = 'L'
            changed = True

   return changed, new_lines

def is_empty(seat):
   return seat == 'L'

def is_occupied(seat):
   return seat == '#'

def count_occupied(lines):
   return len([True for line in lines for seat in line if is_occupied(seat)])