import re

class Node:
   def __init__(self, value):
      self.value = value
      self.next_node = None
      self.lower_node = None
   
   def __repr__(self):
      adds = []
      if self.next_node:
         adds.append(f'n {self.next_node.value}')
      if self.lower_node:
         adds.append(f'l {self.lower_node.value}')

      s = f'{self.value}'
      if len(adds) > 0:
         s += f" -> {'; '.join(adds)}"
      return f'({s})'

def calculate(cups, count, mx=1000000):
   prev_node = None
   h_nodes = {}
   for x in cups:
      node = Node(int(x))
      h_nodes[int(x)] = node
      if prev_node:
         prev_node.next_node = node
      prev_node = node

   for node in h_nodes.values():
      if node.value == 1:
         continue

      node.lower_node = h_nodes[node.value-1]

   first_node = h_nodes[int(cups[0])]
   last_node = h_nodes[int(cups[-1])]
   node1 = h_nodes[1]
   node9 = h_nodes[9]
   print("first_node", first_node)
   print("last_node", last_node)
   print("node1", node1)
   print("node9", node9)

   # mx = 9
   prev_node = last_node
   lw_node = node9
   for x in range(10, mx+1):
      node = Node(x)
      prev_node.next_node = node
      node.lower_node = lw_node
      prev_node = node
      lw_node = node
   
   last_node = prev_node
   last_node.next_node = first_node
   node1.lower_node = lw_node

   print('------')
   print("first_node", first_node)
   print("last_node", last_node)
   print("node1", node1)

   current_node = first_node
   for i in range(count):
      if i % 100000 == 0:
         print(f'{i}: {current_node}')
      current_node = move(current_node)

   cup1_next1 = node1.next_node
   cup1_next2 = cup1_next1.next_node
   return cup1_next1.value, cup1_next2.value


def pp_next(node, count):
   lst = []
   for _ in range(count):
      lst.append(str(node))
      if not node.next_node:
         break
      node = node.next_node
   print(', '.join(lst))

def get_nodes(node, count):
   for _ in range(count):
      node = node.next_node
      yield node

# (3) [8  9  1]  5  4  6  7  {2}
# (3) [8  9  1]  {2}  5  4  6  7 
# (3) [8  9  1]  5  4  {2}  6  7
def move(current_node):
   three_nodes = list(get_nodes(current_node, 3))
   three_cups = [node.value for node in three_nodes]
   
   destination_cup = current_node.lower_node
   # print("destination_cup", destination_cup)
   while destination_cup.value in three_cups:
      destination_cup = destination_cup.lower_node
      # print("destination_cup", destination_cup)

   current_node.next_node = three_nodes[-1].next_node
   nn = destination_cup.next_node
   destination_cup.next_node = three_nodes[0]
   three_nodes[-1].next_node = nn
   return current_node.next_node
