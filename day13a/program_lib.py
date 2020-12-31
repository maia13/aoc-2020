import re


def calculate(file_name):
   fo = open(file_name, "r+")
   line1, line2 = fo.readlines()
   ts = int(line1)
   ids = [int(x) for x in line2.split(',') if x != 'x']

   nexts = [(next_bus_wait(iid, ts), iid) for iid in ids]
   minn = sorted(nexts, key=lambda tuple: tuple[0])[0]

   return minn[0]* minn[1]

def next_bus_wait(iid, ts):
   return int((ts+iid-1)/iid) * iid - ts
