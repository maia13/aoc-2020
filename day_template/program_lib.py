import re


def calculate(file_name):
   fo = open(file_name, "r+")
   lines = [parse_line(line.strip()) for line in fo.readlines()]
   total = 0
   for line in lines:
      pass

   return lines

def parse_line(line):
   return line
