import re
from collections import defaultdict


def calculate(file_name, rn = 20, nt = 25, your = 22):
   fo = open(file_name, "r+")
   lines = [line.strip() for line in fo.readlines()]
   rules_arr = [False] * 1000
   rules = []
   for i in range(rn):
      matched = re.match(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)', lines[i])
      rule_name = matched[1]
      a1, b1 = int(matched[2]), int(matched[3])
      a2, b2 = int(matched[4]), int(matched[5])
      rules.append([(a1, b1), (a2, b2), rule_name])
      for j in range(a1, b1+1):
         rules_arr[j] = True
      for j in range(a2, b2+1):
         rules_arr[j] = True

   your_ticket = [int(n) for n in lines[your].split(',')]

   numbers = [0] * 1000
   neighbor_tickets = []
   num_tickets_dict = defaultdict(list)
   for i in range(nt, len(lines)):
      ticket = [int(n) for n in lines[i].split(',')]
      neighbor_tickets.append(ticket)
      for n in ticket:
         num_tickets_dict[n].append(ticket)
         numbers[n] += 1

   print("your ticket", your_ticket)
   print("neighbor_tickets", len(neighbor_tickets))

   zz = zip(numbers, rules_arr)
   total = 0
   for i, (n, r) in enumerate(zz):
      if n > 0 and not r: # invalid number
         total += i * n
         for ticket in num_tickets_dict[i]:
            # print('to remove', i, ticket)
            if ticket in neighbor_tickets:
               neighbor_tickets.remove(ticket)

   # print("valid", neighbor_tickets)
   tickets = list(neighbor_tickets)
   tickets.append(your_ticket)
   # print("all valid", tickets)
   # print("rules", rules)

   field_names = find_field_names(rules, tickets)
   for names in field_names:
      print("field name:", names)

   total = 1
   for i, name in enumerate(field_names):
      if name.startswith('departure'):
         total *= your_ticket[i]

   return total

def find_field_names(rules, tickets):
   field_names = [None] * len(rules)
   for i in range(len(field_names)):
      field_names[i] = []
      column = [ticket[i] for ticket in tickets]
      for (ra1, rb1), (ra2, rb2), rname in rules:
         if all([ra1 <= n <= rb1 or ra2 <= n <= rb2 for n in column]):
            field_names[i].append(rname)

   changed = True

   while changed:
      changed = False
      one_occurance = [names for names in field_names if len(names) == 1]
      # print("one_occurance", one_occurance)

      for names in field_names:
         for oos in one_occurance:
            if oos != names and oos[0] in names:
               changed = True
               names.remove(oos[0])

   return [names[0] for names in field_names]