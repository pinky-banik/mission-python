num =0
while num != 'quit':
  num = input("please enter any number: ")
  if(num == 'quit'):
    break
  elif(int(num) <0):
    print("the number is negative")
  elif(int(num)>0):
    print("the number is positive")
  elif(int(num)==0):
    print("the number is equal to zero")
  