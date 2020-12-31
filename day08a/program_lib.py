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
   accumulator = 0
   position = 0
   name, value, ran = instructions[position]
   while not ran:
      instructions[position] = (name, value, True)
      accumulator, position = inst_hash[name](value, position, accumulator)
      name, value, ran = instructions[position]
   return accumulator

# nop +0
# acc +1
# jmp +4
def parse_instruction(line):
   matched = re.match(r'^([a-z]{3}) ([+-]\d+)$', line)
   return (matched[1], int(matched[2]), False)
