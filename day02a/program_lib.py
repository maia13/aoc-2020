import re


def calculate():
   fo = open("data.txt", "r+")
   lines = fo.readlines()
   total = 0
   for line in lines:
      if is_valid(line.strip()):
         total += 1

   return total

def is_valid(value):
   matched = re.match(r'^(\d+)-(\d+) ([a-z]): (.*)$', value)
   start = int(matched[1])
   end = int(matched[2])
   letter = matched[3]
   password = matched[4]
   c = count_in(letter, password)
   return start <= c and c <= end

def count_in(letter, text):
   return sum(1 for x in text if x == letter)