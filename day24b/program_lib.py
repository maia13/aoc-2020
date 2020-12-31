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

   for _ in range(100):
      tiles = conways_game_turn(tiles, movement_hash)

   print(tiles)
   return sum(black for _, black in tiles.items())

def conways_game_turn(tiles, movement_hash):
   add_whites_arround_blacks(tiles, movement_hash)
   new_tiles = defaultdict(bool)
   tiles_copy = [(tile, black) for tile, black in tiles.items()]

   for tile, black in tiles_copy:
      neighbors = get_neighbors(movement_hash, tile)
      black_tiles_count = sum(tiles[n] for n in neighbors)
      if black: 
         if black_tiles_count == 0 or black_tiles_count > 2:
            # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
            # => do not copy to the new tiles
            pass
         else:
            # stays black
            # => copy to new tiles
            new_tiles[tile] = True
      else: # white
         if black_tiles_count == 2:
            # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
            new_tiles[tile] = True
   return new_tiles


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
      coos = move(movement_hash, coos, dr)
   return coos


def move(movement_hash, coos, direction):
   x, y = coos
   return movement_hash[y % 2][direction](x, y)

def get_neighbors(movement_hash, tile):
   neighbors = ['ne', 'e', 'se', 'sw', 'w', 'nw']
   return [move(movement_hash, tile, n) for n in neighbors]   

def add_whites_arround_blacks(tiles, movement_hash):
   blacks = [tile for tile, black in tiles.items() if black]
   for tile in blacks:
      neighbors = get_neighbors(movement_hash, tile)
      for n in neighbors:
         if n not in tiles:
            tiles[n] = False # white
