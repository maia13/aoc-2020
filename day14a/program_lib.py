import re

def calculate(file_name):
   fo = open(file_name, "r+")
   lines = fo.readlines()
   memory = []
   mask = (0, 1)
   for line in lines:
      line = line.strip()
      matched_mask = re.match(r'^mask = (.*)$', line)
      if matched_mask:
         mask = matched_mask[1]
         continue

      matched_command = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
      if matched_command:
         index = int(matched_command[1])
         value = int(matched_command[2])
         memory = ensure_memory(memory, index)
         memory[index] = apply_mask(mask, value)

   return sum(memory)

def ensure_memory(memory, index):
   if len(memory) <= index:
      memory += [0] * (index - len(memory) + 1)
   return memory

def apply_mask(mask, value):
   door = ''.join(['1' if x == '1' else '0' for x in mask])
   doand = ''.join(['0' if x == '0' else '1' for x in mask])
   result = (value | int(door, base=2)) & int(doand, base=2)
   return result