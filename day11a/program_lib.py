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

def neighbours(lines, x, y, width, height):
   neighbour_pos = [
      (x-1, y-1), (x, y-1), (x+1, y-1),
      (x-1, y), (x+1, y),
      (x-1, y+1), (x, y+1), (x+1, y+1)
      ]
   return [(a, b) for a, b in neighbour_pos if a >= 0 and b >= 0 and a < width and b < height]

def count_occupied_around(lines, x, y, width, height):
   n = neighbours(lines, x, y, width, height)
   return len([True for a, b in n if lines[b][a] == "#"])

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