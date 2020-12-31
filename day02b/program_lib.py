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
   pos1 = int(matched[1]) - 1
   pos2 = int(matched[2]) - 1
   letter = matched[3]
   password = matched[4]
   return (password[pos1] == letter) ^ (password[pos2] == letter)

