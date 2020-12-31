import re

# 283 too low
# 29506 too low
def calculate():
   return calc("data.txt")

def calc(file_name):
   fo = open(file_name, "r+")
   rows = [parse_line(line.strip()) for line in fo.readlines()]

   total = 0
   search = [(1, 'shiny gold')]
   while len(search) > 0:
      search2 = []
      for n, name in search:
         total += n
         children = [(nn*n, nname) for nn, nname in find_children(name, rows)]
         search2 += children
      search = search2
   
   return total - 1

# bright beige bags contain 4 faded magenta bags, 1 dotted purple bag, 2 mirrored cyan bags, 1 drab white bag.
# faded maroon bags contain no other bags.
def parse_line(line):
   matched = re.match(r'^(.*) bags contain (.*)$', line)
   subject = matched[1]
   children = [x.strip('.') for x in matched[2].split(', ')]

   if len(children) == 1 and children[0] == 'no other bags':
      return subject, []

   return subject, [parse_bag(bag) for bag in children]
   
def find_children(parent, rows):
   return [ch for par, chs in rows for ch in chs if par == parent]

# 4 faded magenta bags
# 1 drab white bag
def parse_bag(bag):
   matched = re.match(r'^(\d+) (.*) bags?$', bag)
   return int(matched[1]), matched[2]


