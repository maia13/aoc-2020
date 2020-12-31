import re

def is_valid_byr(value):
   if re.match(r'^\d+$', value):
      x = int(value)
      if 1920 <= x and x <= 2002:
         return True
   return False

def is_valid_iyr(value):
   if re.match(r'^\d+$', value):
      x = int(value)
      if 2010 <= x and x <= 2020:
         return True
   return False

def is_valid_eyr(value):
   if re.match(r'^\d+$', value):
      x = int(value)
      if 2020 <= x and x <= 2030:
         return True
   return False

def is_valid_hgt(value):
   matched = re.match(r'^(\d+)(cm|in)$', value)
   if matched:
      if matched[2] == 'cm':
         x = int(matched[1])
         if 150 <= x and x <= 193:
            return True
      else:
         x = int(matched[1])
         if 59 <= x and x <= 76:
            return True
   return False

def is_valid_hcl(value):
   if re.match(r'^#[0-9a-f]{6}$', value):
      return True
   return False

def is_valid_ecl(value):
   if re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', value):
      return True
   return False

def is_valid_pid(value):
   if re.match(r'^\d{9}$', value):
      return True
   return False


required_fields = {'byr': 0, 'iyr': 1, 'eyr': 2, 'hgt': 3, 'hcl': 4, 'ecl': 5, 'pid': 6} # cid
required_fields_validation = {'byr': is_valid_byr, 'iyr': is_valid_iyr, 'eyr': is_valid_eyr, 'hgt': is_valid_hgt, 'hcl': is_valid_hcl, 'ecl': is_valid_ecl, 'pid': is_valid_pid} # cid

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
      else:
         pwd_fields += parse_fields(line)

   if is_valid(pwd_fields):
      total += 1

   return total

def parse_fields(st):
   return [kv.split(':') for kv in st.split(' ')]

def is_valid(fields):
   hash = 0
   for field_key, field_value in fields:
      num = required_fields.get(field_key)
      if num != None:
         if not required_fields_validation[field_key](field_value):
            return False
         hash |= 2**num         
   return hash == 2**7-1

