import re
from collections import Counter, defaultdict
import math
from itertools import product

def calculate(file_name):
   fo = open(file_name, "r+")
   square_size = 10
   lines = [line.strip() for line in fo.readlines()]
   squares = get_squares(lines, square_size)
   pph(squares, "squares")

   sidess = {idx: square_as_sides(square) for idx, square in squares.items()}
   pph(sidess, "sidess")

   options = {}
   super_transform_hash = {}
   for idx, sides in sidess.items():
      opts, transform_hash = get_options(sides)
      super_transform_hash |= transform_hash
      options[idx] = opts
   # options = {idx: get_options(sides) for idx, sides in sidess.items()}
   pph(options, "options")

   side_tile = defaultdict(lambda: defaultdict(list))
   for idx, opts in options.items():
      for option in opts:
         for side in option:
            side_tile[side][idx].append(option)

   print("-----------------")
   tile_idxs = []
   sides_out = set()
   tileout_side_options = defaultdict(lambda: defaultdict(list))
   for side, d in side_tile.items():      
      # print(side, len(d))
      if len(d) == 1: # sides facing out
         sides_out.add(side)
         for tile_idx, opts in d.items():
            print("--", side, tile_idx, opts)
            tile_idxs.append(tile_idx)
            tileout_side_options[tile_idx][side] = opts
      # for tile_idx, options in d.items():
      #    print(f"{side} | {tile}")

   # princt("---------- side_tile", side_tile)
   ccc = Counter(tile_idxs)
   corner_tiles = [x for x, count in ccc.items() if count == 4]
   print("corner_tiles", corner_tiles)
   side_tiles = [x for x, count in ccc.items() if count == 2]
   print("side_tiles", side_tiles, len(side_tiles))
   middle_tiles = [key for key in list(options.keys()) if key not in corner_tiles and key not in side_tiles]
   print("middle_tiles", middle_tiles, len(middle_tiles))
   print("sides_out", sides_out)

   # prepare puzzle grid
   puzzle_size = int(math.sqrt(len(squares)))
   puzzle = [None] * puzzle_size
   for i in range(puzzle_size):
      puzzle[i] = [None] * puzzle_size

   # find bottom row
   left_bottom_corner = find_left_bottom_corner(corner_tiles, tileout_side_options, sides_out)
   print("left bottom corner", left_bottom_corner)
   left_bottom_corner_tile_idx, left_bottom_corner_sides = left_bottom_corner
   del options[left_bottom_corner_tile_idx]
   i = 0
   puzzle[0][i] = left_bottom_corner

   possible_bottom_tiles = list(find_all_with_side("left", get_side("right", left_bottom_corner_sides), options))
   while len(possible_bottom_tiles) > 0:
      # print("possible_bottom_tiles", possible_bottom_tiles)
      if len(possible_bottom_tiles) > 1:
         raise Exception("Too many options")
      bottom_tile_ix, bottom_tile_sides = possible_bottom_tiles[0]
      del options[bottom_tile_ix]
      i += 1
      puzzle[0][i] = (bottom_tile_ix, bottom_tile_sides)

      possible_bottom_tiles = list(find_all_with_side("left", get_side("right", bottom_tile_sides), options))      

   ppz(puzzle)

   # find left tiles
   possible_left_tiles = list(find_all_with_side("bottom", get_side("top", puzzle[0][0][1]), options))
   i = 0
   while len(possible_left_tiles) > 0:
      # print(possible_left_tiles)
      if len(possible_left_tiles) > 1:
         raise Exception("Too many options")

      left_tile_ix, left_tile_sides = possible_left_tiles[0]
      del options[left_tile_ix]
      i += 1
      puzzle[i][0] = (left_tile_ix, left_tile_sides)
      possible_left_tiles = list(find_all_with_side("bottom", get_side("top", left_tile_sides), options))

   ppz(puzzle)

   # find all rows
   for row in range(1, puzzle_size):
      col = 0
   
      possible_row_tiles = list(find_all_with_side("left", get_side("right", puzzle[row][col][1]), options))
      while len(possible_row_tiles) > 0:
         # print("possible_row_tiles", possible_row_tiles)
         if len(possible_row_tiles) > 1:
            raise Exception("Too many options")
         row_tile_ix, row_tile_sides = possible_row_tiles[0]
         del options[row_tile_ix]
         col += 1
         puzzle[row][col] = (row_tile_ix, row_tile_sides)

         possible_row_tiles = list(find_all_with_side("left", get_side("right", row_tile_sides), options))      
      ppz(puzzle)

   # find and transform the whole original squares
   puzzle_squares = [None] * puzzle_size
   for i in range(puzzle_size):
      puzzle_squares[i] = [None] * puzzle_size
   for r, row in list(enumerate(puzzle))[::-1]:
      print(r, row)
      for cl, (tile_ix, sides) in enumerate(row):
         print(f"({cl}, {r}):")
         print(f"      tile & option: {tile_ix}, {sides}")
         square = squares[tile_ix]
         print(f"      original square: {tile_ix} -> {square}")
         trans_def = super_transform_hash[sides][0]
         print(f"      transformation: {sides} -> {trans_def}")
         new_square = transform(square, trans_def)
         print(f"      transformed square: {new_square}")
         puzzle_squares[r][cl] = [row[1:-1] for row in new_square[1:-1]]

   print('----------------')
   picture = []
   for row in puzzle_squares[::-1]:
      big_rows = list(zip(*row))
      for big_row in big_rows:
         rr = ''.join(['#' if x == '1' else ' ' for x in ''.join(big_row)])
         picture.append(rr)
         print(rr)

   picture_options = [picture]
   for i in range(3):
      picture_options.append(trans_rotation(picture, i))
   for i in range(4):
      picture_options.append(trans_flip(picture, i))

   monster_coos, monster_width, monster_height = get_monster()
   print("monster", monster_coos, monster_width, monster_height)
   for i, picture_option in enumerate(picture_options):
      picture_monster_coos = []      
      for y in range(len(picture_option)-monster_height):
         for x in range(len(picture_option[0])-monster_width):
            picture_monster_coos = add_picture_monster_coos(picture_monster_coos, (x, y), monster_coos, picture_option)

      print(f"{i}, picture_monster_coos", picture_monster_coos)
      pcoos = set(picture_monster_coos)
      if len(pcoos) > 0:
         axis = list(range(len(picture_option)))
         all_coos = product(axis, axis)
         not_monster_hash_coos = [(x, y) for x, y in all_coos if picture_option[y][x] == '#' and (x, y) not in pcoos]
         return len(not_monster_hash_coos)


   return -1

def add_picture_monster_coos(picture_monster_coos, top_left_corner_coos, monster_coos, picture):
   top_left_x, top_left_y = top_left_corner_coos
   for x, y in monster_coos:
      if picture[top_left_y + y][top_left_x + x] != '#':
         return picture_monster_coos # not a monster here
   # this is a monster
   picture_monster_coos += [(mcoox + top_left_x, mcooy + top_left_y) for mcoox, mcooy in monster_coos]
   return picture_monster_coos

def trans_rotation(square, num):
   for _ in range(num+1):
      square = list(zip(*square[::-1]))
   return [''.join(row) for row in square]

def trans_flip(square, num):
   # yield (bottom, right[::-1], top, left[::-1]) # -
   if num == 0:
      return square[::-1]
   # yield (top[::-1], left, bottom[::-1], right) # |
   if num == 1:
      return [row[::-1] for row in square]
   # yield (right[::-1], top[::-1], left[::-1], bottom[::-1]) # /
   if num == 2:
      # 123    963
      # 456 -> 852
      # 789    741
      return [''.join(row) for row in zip(*[row[::-1] for row in square[::-1]])]
   # yield (left, bottom, right, top) # \
   if num == 3:
      # 123    147
      # 456 -> 258
      # 789    369
      return [''.join(row) for row in zip(*square)]
   
   raise Exception('Should never happen')

transform_h = {
   'original': lambda sq, _ : sq,
   'rotation': trans_rotation,
   'flip': trans_flip
}

def transform(square, trans):
   fnc_name, num = trans
   return transform_h[fnc_name](square, num)

def get_side(side_name, sides):
   top, right, bottom, left = sides
   sw = {
      "top": top,
      "right": right,
      "bottom": bottom,
      "left": left
   }
   return sw[side_name]

def find_all_with_side(side_name, side, options):
   for idx, opts in options.items():
      for opt in opts:
         if get_side(side_name, opt) == side:
            yield (idx, opt)

def find_left_bottom_corner(corner_tiles, tileout_side_options, sides_out):
   # top, right, bottom, left
   for tile_idx in corner_tiles:
      for _, opts in tileout_side_options[tile_idx].items():
         for sides in opts:
            _, _, bottom, left = sides
            if bottom in sides_out and left in sides_out:
               return tile_idx, sides
   raise Exception('Should not get here')

def ppz(puzzle):
   print('------')
   for row in puzzle[::-1]:      
      print([el[0] if el != None else None for el in row])

def pph(hash, name):
   print(f'------ {name}')
   for ix, val in hash.items():
      print(ix, val)

def get_squares(lines, square_size):
   squares = {}
   square = None
   for i, line in enumerate(lines):
      if i % (square_size+2) == 0:
         matched = re.match(r'^Tile (\d+):$', line)
         idx = int(matched[1])
         square = []
         squares[idx] = square
         continue
      if line:
         square.append(''.join(['1' if x == '#' else '0' for x in line]))
         # square.append(line)
      
   return squares

def get_options(sides):
   transform_hash = defaultdict(list)

   int_sides = to_ints(sides)
   options = [int_sides]

   transform_hash[int_sides].append(("original", 0))

   rotations = list(get_rotations(*sides))
   int_rotations = [to_ints(option) for option in rotations]
   options += int_rotations

   for i, int_rot in enumerate(int_rotations):
      transform_hash[int_rot].append(("rotation", i))
   
   flips = list(get_flips(*sides))
   int_flips = [to_ints(option) for option in flips]
   options += int_flips
   for i, int_flip in enumerate(int_flips):
      transform_hash[int_flip].append(("flip", i))

   for i, flip in enumerate(flips):
      int_flip_rotations = [to_ints(option) for option in list(get_rotations(*flip))]
      options += int_flip_rotations
      for j, int_flip_rot in enumerate(int_flip_rotations):
         transform_hash[int_flip_rot].append(f"flip {i}, rotation {j}")

   return set(options), transform_hash

def to_ints(sides):
   return tuple([binint(side) for side in sides])

# ['..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###']
#
# 123
# 456
# 789
# top 123, right 369, bottom 789, left 147
def square_as_sides(square):
   top = square[0]
   right = ''.join([row[-1] for row in square])
   bottom = square[-1]
   left = ''.join([row[0] for row in square])
   return top, right, bottom, left

def get_rotations(top, right, bottom, left):
   yield (left[::-1], top, right[::-1], bottom)
   yield (bottom[::-1], left[::-1], top[::-1], right[::-1])
   yield (right, bottom[::-1], left, top[::-1])

def get_flips(top, right, bottom, left):
   yield (bottom, right[::-1], top, left[::-1]) # -
   yield (top[::-1], left, bottom[::-1], right) # |
   yield (right[::-1], top[::-1], left[::-1], bottom[::-1]) # /
   yield (left, bottom, right, top) # \


def binint(s):
   if type(s) is list:
      return int(''.join(s), base=2)
   return int(s, base=2)

def get_monster():
   monster_picture = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
   monster_width = len(monster_picture[0])
   monster_height = len(monster_picture)
   monster_coos = []
   for y, row in enumerate(monster_picture):
      for x, v in enumerate(row):
         if v == '#':
               monster_coos.append((x, y))
   return monster_coos, monster_width, monster_height