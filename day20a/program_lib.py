
import re
from collections import Counter, defaultdict

def calculate(file_name):
   fo = open(file_name, "r+")
   square_size = 10
   lines = [line.strip() for line in fo.readlines()]
   squares = get_squares(lines, square_size)
   pph(squares)

   sidess = {idx: square_as_sides(square) for idx, square in squares.items()}
   pph(sidess)

   options = {idx: get_options(sides) for idx, sides in sidess.items()}
   pph(options)

   side_tile = defaultdict(lambda: defaultdict(list))
   for idx, options in options.items():
      for option in options:
         for side in option:
            side_tile[side][idx].append(option)

   print("-----------------")
   tile_idxs = []
   for side, d in side_tile.items():
      # print(side, len(d))
      if len(d) == 1:
         for tile_idx, options in d.items():
            # print("--", side, tile_idx, options)
            tile_idxs.append(tile_idx)
      # for tile_idx, options in d.items():
      #    print(f"{side} | {tile}")

   # princt("---------- side_tile", side_tile)
   ccc = [x for x, count in Counter(tile_idxs).items() if count == 4]
   print(ccc)
   return ccc[0] * ccc[1] * ccc[2] * ccc[3]

# # {(0, 0): (2311, (616, 300, 318, 924))}
# def find_neighbors(solution):
#    all_coos = list(solution.keys())

def go_over_solutions():
   # a solution
   # {coos: (tile id, option), ....}
   tile_id = list(options.keys())[0]
   tile_option = list(options[tile_id])[0]
   solutions = [{(0, 0): (tile_id, tile_option)}]

   while len(solutions) > 0:
      solution = solutions[0]
      solutions = solutions[1:]

      break

   print("solutions", solutions)

def pph(hash):
   print('------')
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
   options = [to_ints(sides)]
   rotations = list(get_rotations(*sides))
   options += [to_ints(option) for option in rotations]

   flips = list(get_flips(*sides))
   options += [to_ints(option) for option in flips]

   for flip in flips:
      options += [to_ints(option) for option in list(get_rotations(*flip))]

   return set(options)

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