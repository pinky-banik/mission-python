with open('message.txt' ,'a') as fileWrite:
  fileWrite.write('Hello from python from pinky')

with open('message.txt','r') as fileRead:
  text= fileRead.read()
  print(text)

