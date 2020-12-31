import re

required_fields = {'byr': 0, 'iyr': 1, 'eyr': 2, 'hgt': 3, 'hcl': 4, 'ecl': 5, 'pid': 6} # cid

def calculate():
   fo = open("data.txt", "r+")
   lines = fo.readlines()
   total = 0
   pwd_fields = []
   for line in lines:
      line = line.strip()
      if line == '':
         if is_valid(pwd_fields):
            total += 1
         pwd_fields = []
      pwd_fields += parse_fields(line)

   if is_valid(pwd_fields):
      total += 1

   return total

def parse_fields(st):
   return [kv.split(':')[0] for kv in st.split(' ')]

def is_valid(fields):
   hash = 0
   for field_key in fields:
      num = required_fields.get(field_key)
      if num != None:
         hash |= 2**num
   return hash == 2**7-1
