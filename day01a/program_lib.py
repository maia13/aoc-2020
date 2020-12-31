import re


def calculate():
   fo = open("data.txt", "r+")
   nums = [int(line.strip()) for line in fo.readlines()]

   for num1 in nums:
      for num2 in nums:
         if num1 + num2 == 2020:
            return num1 * num2

   raise Exception('It should have gone here')

