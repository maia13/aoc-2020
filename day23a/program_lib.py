import re


def calculate(cups, count):
   for _ in range(count):
      cups = move(cups)

   ix1 = cups.index('1')
   result = cups[ix1+1:] + cups[0:ix1]
   return ''.join(result)

# (3) [8  9  1]  5  4  6  7  {2}
# (3) [8  9  1]  {2}  5  4  6  7 
# (3) [8  9  1]  5  4  {2}  6  7
def move(cups):
   current_cup_label = cups[0]
   three_cups = cups[1:4]
   destination_cup_label = int(current_cup_label) - 1
   while str(destination_cup_label) in three_cups or destination_cup_label == 0:
      if destination_cup_label < 0:
         raise Exception(f'destination_cup_label = {destination_cup_label}')

      if destination_cup_label == 0:
         destination_cup_label = 9
      else:
         destination_cup_label -= 1

   destination_cup_ix = cups.index(str(destination_cup_label))
   result_cups = cups[4:destination_cup_ix+1] + three_cups + cups[destination_cup_ix+1:] + current_cup_label
   return result_cups
