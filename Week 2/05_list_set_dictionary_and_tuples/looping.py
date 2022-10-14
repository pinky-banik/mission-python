# # looping in list
# numbers = [12,45,65,23,89,78,45,11]
# total = sum(numbers)
# total = 0
# for i in numbers:
#   total = total + i
#   print(i)
# print (total)

# # to get the index with while loop
# for num in enumerate(numbers):
#   print(num)

# looping in set

# nums = {12,45,65,23,89,78,45,11}

# set_total = 0
# for num in nums :
#   set_total += num
# print(set_total)

# # looping in tuples

# number_tuples = 12,45,65,23,89,78,11,45
# # if we just declare some values with commas than its a tuple

# tuples_total =0
# for num in number_tuples:
#   tuples_total +=num
# print(tuples_total)

# looping in dictionary
marks = { 'physics' : 12, 'chemistry' : 45 , 'math' : 56 }

# looping in dictionary only loop through the keys
for mark in marks:
  val = marks[mark]
  print(mark,val) 

for subject,mark in marks.items():
  print(subject,mark)
