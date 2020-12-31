import re
from collections import defaultdict

def calculate(file_name):
   fo = open(file_name, "r+")
   lines = fo.readlines()
   memory = defaultdict(int)
   parsed_mask = None
   mask = None
   for i, line in enumerate(lines):
      line = line.strip()
      # print(f"{i:3d}: {line}")
      matched_mask = re.match(r'^mask = (.*)$', line)
      if matched_mask:
         mask = matched_mask[1]
         parsed_mask = parse_mask(mask)
         continue

      matched_command = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
      if matched_command:
         index = int(matched_command[1])
         value = int(matched_command[2])
         addresses = get_addresses(parsed_mask, index)
         for address in addresses:
            memory[address] = value

   return sum(memory.values())

def ensure_memory(memory, index):
   if len(memory) <= index:
      memory += [0] * (index - len(memory) + 1)
   return memory

def get_addresses(mask, address):
   bits_to_override1, bits_to_zero, fluid = mask
   result = address | bits_to_override1
   result &= bits_to_zero

   lst = [result]
   for f in fluid:
      lst2 = []
      for x in lst:
         lst2.append(x)
         lst2.append(x | f)
      lst = lst2
   
   return lst

def parse_mask(mask):
   bits_to_override1 = binary_to_int([m if m == '1' else '0' for m in mask])
   bits_to_zero = binary_to_int(['0' if m == 'X' else '1' for m in mask])
   fluid = [2**(35-i) for i, m in enumerate(mask) if m == 'X']
   return bits_to_override1, bits_to_zero, fluid

def binary_to_int(b):
   if type(b) is list:
      return int(''.join(b), base=2)
   return int(b, base=2)

def int_to_binary(num):
   return f'{num:b}'.zfill(36)
