import re
import itertools

class Node:
   def __init__(self, idx, data):
      self.idx = idx
      self.data = data
      self.options = []
   
   def __repr__(self):
      return f'Node {self.idx}: {self.data}, options {len(self.options)}'
   
   def calculate_all(self, indent = 0):
      # print('-' * indent,'calculate_all', self)
      if len(self.options) == 0:
         # print(' ' * indent, '-> ', [self.data])
         return [self.data] # [a] or [b]
      result = []
      for option in self.options:
         x = [node.calculate_all(indent+2) for node in option]
         # print(' ' * indent, '-> x: ', x)
         res_option = [''.join(y) for y in list(itertools.product(*x))]
         result += res_option
      # print(' ' * indent, '->', result)
      return result


def calculate(file_name, n):
   fo = open(file_name, "r+")
   lines = fo.readlines()
   nodes_list = [parse_line(line.strip()) for line in lines[0:n]]
   nodes_dict = { node.idx:node for node in nodes_list}
   root = nodes_dict[0]
   for node in nodes_list:
      if node.data in ['a', 'b']:
         print(node)
         continue

      for opt in node.data:
         node.options.append([nodes_dict[idx] for idx in opt])
      print(node)
   print("Root:", root)
   res = set(root.calculate_all())

   total = 0
   received_messages = [line.strip() for line in lines[n+1:]]
   for m in received_messages:
      if m in res:
         total += 1
      
   # print("Calc all:", res)

   return total

# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
def parse_line(line):
   # 1: "a"
   # 3: "b"
   matched = re.match(r'^(\d+): \"([ab])\"$', line)
   if matched:
      return Node(int(matched[1]), matched[2])
   
   # 0: 1 2
   # 2: 1 3 | 3 1
   matched = re.match(r'^(\d+): (.*)$', line)
   if matched:
      idx = int(matched[1])
      rest =[tuple([int(y) for y in x.strip().split(' ')]) for x in matched[2].split('|')]
      return Node(idx, rest)

   raise Exception('Should not get here')
