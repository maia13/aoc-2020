import re
from collections import defaultdict

def calculate(file_name):
   fo = open(file_name, "r+")
   lines = [line.strip() for line in fo.readlines()]
   movement_hash = get_movement_hash()
   reference_tile = (0, 0)
   tiles = defaultdict(bool)

   for line in lines:
      tile = move_line(movement_hash, line, reference_tile)
      tiles[tile] = not tiles[tile]

   print(tiles)
   return sum(black for _, black in tiles.items())

# sesenwnenenewseeswwswswwnenewsewsw
# e, se, sw, w, nw, and ne
def get_direction(line):
   if line[0] in ['s', 'n']:
      return line[0:2], line[2:]
   
   return line[0], line[1:]

def get_movement_hash():
   return {
      0: {
         'ne': lambda x, y: (x+1, y+1),
         'e': lambda x, y: (x+1, y),
         'se': lambda x, y: (x+1, y-1),
         'sw': lambda x, y: (x, y-1),
         'w': lambda x, y: (x-1, y),
         'nw': lambda x, y: (x, y+1)
      },
      1: {
         'ne': lambda x, y: (x, y+1),
         'e': lambda x, y: (x+1, y),
         'se': lambda x, y: (x, y-1),
         'sw': lambda x, y: (x-1, y-1),
         'w': lambda x, y: (x-1, y),
         'nw': lambda x, y: (x-1, y+1)
      }
   }

def move_line(movement_hash, line, coos):
   while len(line) > 0:
      dr, line = get_direction(line)
      prev_tile = coos
      coos = move(movement_hash, coos, dr)
      print(prev_tile, dr, coos)
   return coos


def move(movement_hash, coos, direction):
   x, y = coos
   return movement_hash[y % 2][direction](x, y)

def print_neighbors(movement_hash):
   neighbors = ['ne', 'e', 'se', 'sw', 'w', 'nw']
   t1 = (0, 0)
   t1x, t1y = t1
   for n in neighbors:
      print(n, t1, movement_hash[t1y % 2][n](t1x, t1y))
   t2 = (0, 1)
   t2x, t2y = t2
   for n in neighbors:
      print(n, t2, movement_hash[t2y % 2][n](t2x, t2y))
