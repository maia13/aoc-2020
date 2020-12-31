import re
import operator
import math

def calculate(file_name):
   fo = open(file_name, "r+")
   lines = fo.readlines()
   total = 0

   for line in lines:
      total += eval_expression(line.strip())

   return total

def eval_expression(line):
   data = parse_line(line)
   # print(data)
   stack = []
   for item in data:
      print('----------', item)
      if item == '(':
         stack.append(item)
         print('stack', stack)
         continue      
      if item == ')':
         expression = stack.pop()
         opening = stack.pop()
         if opening != '(':
            raise Exception('( expected')
         print('popped exp', expression)
         print('stack', stack)
         result = eval_simple_expression(expression)
         push_to_stack(stack, result)
         continue
      
      push_to_stack(stack, item)
      print('stack', stack)

   return eval_simple_expression(stack[-1])

def push_to_stack(stack, value):
   if len(stack) == 0 or stack[-1] == '(':
      stack.append([])
   stack[-1].append(value)


def eval_simple_expression(expression):
   if len(expression) == 0:
      return 0
   addends = []
   i = 0
   while i < len(expression):
      x = expression[i]
      i += 1
      if x == '+':
         addends[-1] += expression[i]
         i += 1
         continue
      if x == '*':
         continue
      addends.append(x)
   
   result = math.prod(addends)
   # print(expression, addends, result)

   return result
   

def parse_line(line):
   splitline = line.replace('(', '( ').replace(')', ' )').split(' ')
   return [item if item in ['(', ')', '*', '+'] else int(item) for item in splitline]
      