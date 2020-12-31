import re

def nop(value, position, accumulator):
   return (accumulator, position+1)

def acc(value, position, accumulator):
   return (accumulator+value, position+1)

def jmp(value, position, accumulator):
   return (accumulator, position+value)

inst_hash = { 'nop': nop, 'acc': acc, 'jmp': jmp }

def calculate(file_name):
   fo = open(file_name, "r+")
   instructions = [parse_instruction(line.strip()) for line in fo.readlines()]
   for i, inst in enumerate(instructions):
      name, value, _ = inst
      try_again = (name == 'jmp' or name == 'nop')
      if try_again:
         inst_copy = [x for x in instructions]
      if name == 'jmp':
         inst_copy[i] = ('nop', value, False)
      if name == 'nop':
         inst_copy[i] = ('jmp', value, False)
      if try_again:
         is_loop, acc = infinite_loop(inst_copy)
         if not is_loop:
            return acc

   raise Exception('Should not get here')

def infinite_loop(instructions):
   accumulator = 0
   position = 0
   while True:
      name, value, ran = instructions[position]
      if ran:
         return True, accumulator
      instructions[position] = (name, value, True)
      accumulator, position = inst_hash[name](value, position, accumulator)
      if position >= len(instructions):
         break
   
   return False, accumulator

# nop +0
# acc +1
# jmp +4
def parse_instruction(line):
   matched = re.match(r'^([a-z]{3}) ([+-]\d+)$', line)
   return (matched[1], int(matched[2]), False)
