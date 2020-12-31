import re
import itertools

def calculate(file_name, n):
   fo = open(file_name, "r+")
   lines = fo.readlines()
   nodes_list = [parse_line(line.strip()) for line in lines[0:n]]
   nodes_dict = { node[0]:node for node in nodes_list}

   # pp(nodes_list)

   received_messages = [line.strip() for line in lines[n+1:]]

   solved_nodes = [node for node in nodes_list if node[2]]
   unsolved_nodes = [node for node in nodes_list if not node[2]]

   while len(unsolved_nodes) > 0:
      for snode in solved_nodes:
         sid, srule, _ = snode
         for unode in unsolved_nodes:
            _, urule, _ = unode
            outrule = combine_rules(sid, srule, urule)
            unode[1] = outrule
            unode[2] = all(type(x) is str for x in outrule)
      prev_uns_count = len(unsolved_nodes)
      solved_nodes = [node for node in nodes_list if node[2]]
      unsolved_nodes = [node for node in nodes_list if not node[2]]
      if len(unsolved_nodes) == 1:
         print('node', unsolved_nodes)
         print('8 len', len(nodes_dict[8][1]))
         print('11 len', len(nodes_dict[11][1]))
      # pp(nodes_list)
      print("solved_nodes", len(solved_nodes), "unsolved_nodes", len(unsolved_nodes))
      if prev_uns_count == len(unsolved_nodes):
         pp(solved_nodes)
         pp(unsolved_nodes)
         break

   print('--------------- 8: 42 | 42 8 ----- 42:', nodes_dict[42])
   print('--------------- 11: 42 31 | 42 11 31 ------ 31:', nodes_dict[31])
   return 0

def pp(nodes_list):
   print('--------------')
   for idx, rules, solved in nodes_list:
      if len(rules) < 10:
         print(idx, solved, rules)
      else:
         print(idx, solved, len(rules))


# srule: [4, ['ab', 'bb'], True]
# urule: [2, [(4, 4), (5, 5)], False]
def combine_rules(sid, srule, urule):
   outorpart = []
   for orpart in urule:
      if type(orpart) is str:
         outorpart.append(orpart)
         continue
      # for andpart in 
      andparts = [handle_andpart(andpart, sid, srule) for andpart in orpart]
      outorpart += [list(x) for x in itertools.product(*andparts)]
   result = [join_terminal_ors(orpart) for orpart in outorpart]
   return result

def join_terminal_ors(lst):
   s = ''
   for x in lst:
      if type(x) is int:
         return lst
      s += x
   return s

def handle_andpart(andpart, sid, srule):
   if andpart == sid:
      return srule
   else:
      return [andpart]

# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
def parse_line(line):
   # 1: "a"
   # 3: "b"
   matched = re.match(r'^(\d+): \"([ab])\"$', line)
   if matched:
      return [int(matched[1]), [matched[2]], True]
   
   # 0: 1 2
   # 2: 1 3 | 3 1
   matched = re.match(r'^(\d+): (.*)$', line)
   if matched:
      idx = int(matched[1])
      rest =[[int(y) for y in x.strip().split(' ')] for x in matched[2].split('|')]
      return [idx, rest, False]

   raise Exception('Should not get here')
