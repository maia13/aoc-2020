import re


def calculate(file_name):
   fo = open(file_name, "r+")
   lines = [line.strip() for line in fo.readlines()]
   minX, minY, minZ = 0, 0, 0
   maxX = len(lines[0])
   maxY = len(lines)
   maxZ = 1
   minmax = [minX, maxX, minY, maxY, minZ, maxZ]
   cubes = {}

   for x in range(maxX):
      for y in range(maxY):
         if lines[y][x] == '#':
            cubes[(x, y, 0)] = '#'

   for i in range(6):
      print(f'After {i+1} cycles:')
      changed, cubes, minmax, active_count = turn(cubes, minX, maxX, minY, maxY, minZ, maxZ)
      minX, maxX, minY, maxY, minZ, maxZ = minmax
      pp(cubes, minX, maxX, minY, maxY, minZ, maxZ)

   return active_count

def pp(cubes, minX, maxX, minY, maxY, minZ, maxZ):
   for z in range(minZ, maxZ):
      print()
      print(f'z={z}')
      for y in range(minY, maxY):
         row = ''
         for x in range(minX, maxX):
            if is_active(cubes, x, y, z):
               row += '#'
            else:
               row += '.'
         print(row)

def neighbours(x, y, z):
   neighbour_pos = []
   for xx in range(-1, 2):
      for yy in range(-1, 2):
         for zz in range(-1, 2):
            neighbour_pos.append((x+xx, y+yy, z+zz))
   neighbour_pos.remove((x, y, z))
   return neighbour_pos


def count_active_around(cubes, x, y, z):
   return len([True for a, b, c in neighbours(x, y, z) if is_active(cubes, a, b, c)])

def expand_boundries(x, y, z, minmax):
   minX, maxX, minY, maxY, minZ, maxZ = minmax
   if x < minX:
      minX = x
   if x >= maxX:
      maxX = x + 1
   if y < minY:
      minY = y
   if y >= maxY:
      maxY = y + 1
   if z < minZ:
      minZ = z
   if z >= maxZ:
      maxZ = z + 1
   return [minX, maxX, minY, maxY, minZ, maxZ]

def turn(cubes, minX, maxX, minY, maxY, minZ, maxZ):
   changed = False
   new_cubes = {}
   new_minmax = [minX, maxX, minY, maxY, minZ, maxZ]
   active_count = 0
   for x in range(minX-1, maxX+1):
      for y in range(minY-1, maxY+1):
         for z in range(minZ-1, maxZ+1):
            active_neighbors = count_active_around(cubes, x, y, z)
            if is_active(cubes, x, y, z):
               if active_neighbors in [2, 3]:
                  new_cubes[(x, y, z)] = '#'
                  active_count += 1
               else:
                  changed = True # from active to inactive
            else:
               if active_neighbors == 3:
                  new_cubes[(x, y, z)] = '#'
                  changed = True
                  new_minmax = expand_boundries(x, y, z, new_minmax)
                  active_count += 1

   return changed, new_cubes, new_minmax, active_count

def is_inactive(cubes, x, y, z):
   return (x, y, z) not in cubes or cubes[(x, y, z)] != '#'

def is_active(cubes, x, y, z):
   return (x, y, z) in cubes and cubes[(x, y, z)] == '#'

def count_actives(cubes, minX, maxX, minY, maxY, minZ, maxZ):
   c = 0
   for x in range(minX, maxX):
      for y in range(minY, maxY):
         for z in range(minZ, maxZ):
            if is_active(cubes, x, y, z):
               c += 1
   return c
