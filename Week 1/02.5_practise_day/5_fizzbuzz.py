i= 1
for i in range (50): 
  num = int(input("please enter any number from 1 to 50: "))
  if(num%3==0 and num%5 == 0):
    print("fizzbuzz")
  elif(num%5 == 0):
    print("buzz")
  elif(num%3 ==0):
    print("fizz")
  else:
    print(num) 