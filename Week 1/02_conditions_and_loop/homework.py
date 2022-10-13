""" 
1. print out odd numbers between 13 to 39
2. use for loop to print numbers between 13 to 39 using and range
3.  print out 20 to 1 using while loop
"""

# 1. print out odd numbers between 13 to 39

num = 13
while num <= 39 :
  if(num % 2 ==1):
    print(num)
  num = num +1 
# 2. use for loop to print numbers between 13 to 39 using and range
for index in range(13,39):
  print(index)

# 3.  print out 20 to 1 using while loop

n = 20
while n >=0 :
  print(n)
  n= n-1
