try:
  numbers = [12,45,65,23,89,78,11]
  numbers_iter = iter(numbers)
  print(next(numbers_iter))
  print(next(numbers_iter))
  print(next(numbers_iter))
  print('I am exploring iterator')
  print(next(numbers_iter))
  print(next(numbers_iter))
  print('Doing something else now')
  print(next(numbers_iter))
  print(next(numbers_iter))
  print(next(numbers_iter))
except:
  print('iteration is stopped')