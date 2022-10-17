def add(a,b):
  sum = a+b
  print(sum)


def deduct(x,y):
  result = x-y
  return result

class phone:
  color = 'black' # class attribute
  features = ['camera','water proof','can be used as a hammer']

  def call(self): # if you create a function inside a class then that is a method
    # you muss a argument o parameter to a method in python class method
    print('ring ring ring')

  def send_sms(self,number,text):
    sms = f'sending sms : {text} to {number}'
    return sms

my_phone = phone()
my_phone.call()
sms = my_phone.send_sms('018000','i missed to miss you')
print(sms)