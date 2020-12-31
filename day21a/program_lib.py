import re
from collections import defaultdict


def calculate(file_name):
   fo = open(file_name, "r+")
   foods = [parse_line(line.strip()) for line in fo.readlines()]
   all_allergens = {}
   all_ings = []

   for food in foods:
      ings, allergs = food
      all_ings += ings
      for allerg in allergs:
         if allerg in all_allergens:
            all_allergens[allerg] &= ings
         else:
            all_allergens[allerg] = set(ings)
      print("food", food)

   ings_with_algs = set([x for xx in all_allergens.values() for x in xx])
   print("all_allergens", all_allergens)
   print("ings_with_algs", ings_with_algs)
   print("all_ings", all_ings)
   return len([x for x in all_ings if x not in ings_with_algs])

# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
def parse_line(line):
   matched = re.match(r'^([^(]*) \(contains ([^)]*)\)$', line)
   if not matched:
      raise Exception(f'Cannot parse: {line}')

   ingredients = set(matched[1].split(" "))
   allergens = set(matched[2].split(", "))
   return (ingredients, allergens)
