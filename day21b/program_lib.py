import re
from collections import defaultdict


def calculate(file_name):
   fo = open(file_name, "r+")
   foods = [parse_line(line.strip()) for line in fo.readlines()]
   all_allergens = {}
   all_ings = []

   for food in foods:
      print("food", food)
      ings, allergs = food
      all_ings += ings
      for allerg in allergs:
         if allerg in all_allergens:
            # print(f"all_allergens[{allerg}] -> {all_allergens[allerg]}")
            all_allergens[allerg] &= ings
            # print(f"all_allergens[{allerg}] &= {ings}")
            # print(f"all_allergens[{allerg}] -> {all_allergens[allerg]}")
         else:
            all_allergens[allerg] = set(ings)
            # print(f"all_allergens[{allerg}] = {ings}")


   print("all_allergens", all_allergens)

   to_solve = all_allergens
   solved = {}
   solved_ingrs = []
   subsolved = {}
   while len(to_solve) > 0:
      # delete solved_ingrs
      for a in to_solve:
         for si in solved_ingrs:
            if si in to_solve[a]:
               to_solve[a].remove(si)

      subsolved, solved_ingrs, to_solve = solved_ings(to_solve)

      # copy new solved to solved result
      for a, ings in subsolved.items():
         solved[a] = ings

      print("solved", solved, solved_ingrs)
      print("to_solve", to_solve)

   result = [list(ings)[0] for a, ings in sorted(solved.items())]
   print(result)
   # ings_with_algs = set([x for xx in all_allergens.values() for x in xx])
   # inert_ings = [x for x in all_ings if x not in ings_with_algs]
   # print("inert_ings", inert_ings)
   return ','.join(result)

# all_allergens {'dairy': {'mxmxvkd'}, 'fish': {'sqjhc', 'mxmxvkd'}, 'soy': {'sqjhc', 'fvjkl'}}
# solved {'dairy': {'mxmxvkd'} }
# to solve { 'fish': {'sqjhc', 'mxmxvkd'}, 'soy': {'sqjhc', 'fvjkl'} }
def solved_ings(all_allergens):
   solved = {a: ings for (a, ings) in all_allergens.items() if len(ings) == 1 }
   solved_ingrs = set([x for xx in solved.values() for x in xx])
   to_solve = {a: ings for (a, ings) in all_allergens.items() if len(ings) != 1 }
   return solved, solved_ingrs, to_solve

# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
def parse_line(line):
   matched = re.match(r'^([^(]*) \(contains ([^)]*)\)$', line)
   if not matched:
      raise Exception(f'Cannot parse: {line}')

   ingredients = set(matched[1].split(" "))
   allergens = set(matched[2].split(", "))
   return (ingredients, allergens)
