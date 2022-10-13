# odd number ==> remainder will be 1 after dividing by 2
# even number ==> remainder will be 0 after dividing by 2

num = 7
while num <= 20 :
  num = num + 1
  if(num % 2 == 1) :
    continue
  print(num)