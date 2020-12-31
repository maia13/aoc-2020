
def calculate(data, number):
   i = 0
   spoken = {}
   last_number_ix = None
   while i < number:
      if i < len(data):
         last_number = data[i]
         last_number_ix = spoken[last_number] if last_number in spoken else None            
         spoken[last_number] = i
         # print(i, last_number)
      elif last_number_ix == None:
         last_number = 0
         last_number_ix = spoken[last_number] if last_number in spoken else None            
         spoken[last_number] = i
         # print(i, last_number)
      else:
         last_number = spoken[last_number] - last_number_ix
         last_number_ix = spoken[last_number] if last_number in spoken else None            
         spoken[last_number] = i
         # print(i, last_number)
      i += 1 

   return last_number

