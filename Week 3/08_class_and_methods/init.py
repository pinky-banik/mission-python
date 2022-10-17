class phone:
  manufactured = 'china' 
  def __init__(self,brand,price,color):
    self.brand = brand
    self.price = price
    self.color = color

  def send_sms(self,number,text):
    sms = f'sending: {text} to {number}'
    return sms

my_phone = phone('oppo',1300,'blue')
print(my_phone.brand)
her_phone = phone('iphone',85000,'purple')
print(her_phone.color)