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
      # print('----------', item)
      if item != ')':
         stack.append(item)
         # print('stack', stack)
      else:
         expression = pop_expression(stack)
         # print('popped exp', expression)
         # print('stack', stack)
         result = eval_simple_expression(expression)
         stack.append(result)

   return eval_simple_expression(stack)

def pop_expression(stack):
   x = stack.pop()
   expression = []
   while x != '(':
      expression.append(x)
      x = stack.pop()
   expression.reverse()
   return expression

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
      