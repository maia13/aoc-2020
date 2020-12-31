import re

# 127 index 14
# 14144619 index 504
# too low 1756999
def calculate(file_name, max_index, number):
   fo = open(file_name, "r+")
   numbers = [int(line.strip()) for line in fo.readlines()]

   for i in range(0, max_index):
      s = 0
      for j in range(i, max_index):
         s += numbers[j]
         if s > number:
            break
         if s == number:
            nums = numbers[i:j+1]
            return min(nums) + max(nums)

   raise Exception('Should not get here')

