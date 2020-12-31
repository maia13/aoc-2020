import re


def calculate(file_name):
   fo = open(file_name, "r+")
   public_keys = [int(parse_line(line.strip())) for line in fo.readlines()]
   print("public_keys", public_keys)
   loop_sizes = [find_loopsize(7, pk) for pk in public_keys]
   print("loop_sizes", loop_sizes)
   return transform(public_keys[1], loop_sizes[0])

def parse_line(line):
   return line

def transform(subject, loop_size):
   value = 1
   for _ in range(loop_size):
      value = (value * subject) % 20201227
   print(f'transform({subject}, {loop_size}) -> {value}')
   return value

def find_loopsize(subject, result):
   print(f'find_loopsize({subject}, {result})')
   loopsize = 0
   value = 1
   while value != result:
      value = (value * subject) % 20201227
      loopsize += 1
   print(f'find_loopsize({subject}, {result}) -> {loopsize}')
   return loopsize