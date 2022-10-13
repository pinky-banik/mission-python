balance = 500 # global scope
def total_cost (price,quantity):
  global balance
  cost = price*quantity #local scope
  remaining = balance - cost
  # balance = remaining # gives error
  # you can use global variable into local scope bt cannot change it
  balance = balance- cost
  print(f"remaining : {remaining}")
  return cost

print (f"balace outside before: {balance}")
pay = total_cost(10,3)
print(f'Please pay: {pay}')
print (f"balace outside after: {balance}")