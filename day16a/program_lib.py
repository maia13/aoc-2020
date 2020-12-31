import re


def calculate(file_name, rn = 20, nt = 25):
   fo = open(file_name, "r+")
   lines = [line.strip() for line in fo.readlines()]
   rules_arr = [False] * 1000
   rules = []
   for i in range(rn):
      matched = re.match(r'^[^:]+: (\d+)-(\d+) or (\d+)-(\d+)', lines[i])
      a1, b1 = int(matched[1]), int(matched[2])
      a2, b2 = int(matched[3]), int(matched[4])
      rules.append([(a1, b1), (a2, b2)])
      for j in range(a1, b1+1):
         rules_arr[j] = True
      for j in range(a2, b2+1):
         rules_arr[j] = True

   numbers = [0] * 1000
   for i in range(nt, len(lines)):
      ns = lines[i].split(',')
      for n in ns:
         numbers[int(n)] += 1

   zz = zip(numbers, rules_arr)
   total = 0
   for i, (n, r) in enumerate(zz):
      if n > 0 and not r:
         total += i * n

   return total

