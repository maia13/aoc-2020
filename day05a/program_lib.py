import re


def calculate():
    fo = open("data.txt", "r+")
    lines = fo.readlines()
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

