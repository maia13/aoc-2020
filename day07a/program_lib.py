
import re


def calculate():
   fo = open("data.txt", "r+")
   rows = [parse_line(line.strip()) for line in fo.readlines()]

   search = {'shiny gold'}
   all_pars = set()
   while len(search) > 0:
      search2 = []
      for ch in search:
         search2 += find_parents(ch, rows)

      for s in search2:
         all_pars.add(s)
      search = search2
   
   return len(all_pars)

# bright beige bags contain 4 faded magenta bags, 1 dotted purple bag, 2 mirrored cyan bags, 1 drab white bag.
# faded maroon bags contain no other bags.
def parse_line(line):
   matched = re.match(r'^(.*) bags contain (.*)$', line)
   subject = matched[1]
   children = re.findall(r'[ ]?\d+ ([^,.]+) bags?[,.]', matched[2])
   return subject, children
   
def find_parents(child, rows):
   return [par for par, chs in rows if child in chs]
