import re


def calculate(file_name, offset):
   fo = open(file_name, "r+")
   numbers = [int(line.strip()) for line in fo.readlines()]
   matrix = sum_matrix(numbers)
   # print(numbers)
   for pos in range(offset, len(numbers)):
      value = numbers[pos]
      v, i, j = is_valid(pos, value, matrix, offset)
      if v:
         pass
         # print(value, i, j, numbers[i], numbers[j])
      if not v:
         return value

   raise Exception('Should not get here')

def sum_matrix(numbers):
   size = len(numbers)   
   matrix = []   
   for i in range(size):
      lst = [None] * size
      matrix.append(lst)
      for j in range(i+1, size):
         lst[j] = numbers[i] + numbers[j]
   return matrix


def is_valid(position, value, matrix, offset):
   start = max(0, position-offset)

   for i in range(start, position):
      for j in range(i+1, position):
         if matrix[i][j] == value:
            return True, i, j
   
   return False, None, None