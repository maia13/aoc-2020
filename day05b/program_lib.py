import re


def calculate():
    fo = open("data.txt", "r+")
    lines = fo.readlines()
    seat_set = {seat_id_from_line(line.strip()) for line in lines}
    x = 72
    while x < 905:
       if x not in seat_set:
         return x
       x += 1

    raise Exception('This should have finished earlier')

# 71
def min(lines):
    total = 1000
    for line in lines:
       row, col = decode(line.strip())
       sid = seat_id(row, col)
       if sid < total:
          total = sid

    return total

# 905
def max(lines):
    total = 0
    for line in lines:
       row, col = decode(line.strip())
       sid = seat_id(row, col)
       if sid > total:
          total = sid

    return total

def decode(st):
   st = re.sub('[FL]', '0', st)
   st = re.sub('[BR]', '1', st)

   row = int(st[0:7], 2)
   col = int(st[7:10], 2)

   return row, col

def seat_id(row, col):
   return row*8 + col

def seat_id_from_line(line):
   row, col = decode(line)
   return seat_id(row, col)

