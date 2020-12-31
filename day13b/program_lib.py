import re


def calculate(file_name, mint):
   fo = open(file_name, "r+")
   _, line2 = fo.readlines()
   return calc(line2, mint)

def calc(line2, mint = 0):
   ids = [(i, int(x)) for i, x in enumerate(line2.split(',')) if x != 'x']
   # print(ids)
   # # (t + 35) % 37 == 0
   # for i, iid in ids:
   #    print(f'(t + {i: >3}) % {iid: >3} == 0')

   # print(f'------------')
   # for u, (i, iid) in enumerate(ids):
   #    print(f'{iid: >3} x{u} - t = {i: >3}')

   print(f'------------')
   result = ''
   for u, (i, iid) in enumerate(ids):
      result += f'{iid}*a_{u}={i}+a_9, '

   print(result)
   return 0
   #
   mi, m = max(ids, key = lambda tuple: tuple[1])
   print(mi, m)
   t = int(mint/m) * m - mi
   print(t)
   c = 0
   while True:
      if is_valid(ids, t):
         return t      
      t += m
      c += 1
      if c % 1000000 == 0:
         print(t)
   
   raise Exception('It should not get here')


def is_valid(ids, t):
   for i, x in ids:
      if (t + i) % x != 0:
         return False
   return True

#41*x_0-0=t,37*x_1-35=t,431*x_2-41=t,23*x_3-49=t,13*x_4-54=t,17*x_5-58=t,19*x_6-60=t,863*x_7-72=t,29*x_8-101=t
