try:
  num = 15/0
  print(num)
except:
  print('something went wrong') # works when try dosent works
finally:
  print('this is done') # always work