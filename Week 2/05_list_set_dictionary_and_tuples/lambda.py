# def square (x):
#   return x*x

# lamba is used for to write function in one line
square = lambda x:x*x 
 # here x is parameters and it returns x*x
result  = square(6)
# print(result)

add = lambda x,y : x+y
# print(add(45,56))

numbers = [ 12,45,65,23,89,78,11]

def double_it(x):
  return x*2

double_it2 = lambda x:x*2

## lambda function with map

# doubled_numbers = map(double_it,numbers)
doubled_numbers = map(lambda x:x*2,numbers)
squared_numbers = map(lambda x:x*x,numbers)
# map(function,values) the function will iterate to every value
# print(numbers)
# print(list(squared_numbers))

# lambda function with filter
# numbers = [ 12,45,65,23,89,78,11]

bigger_numbers = filter(lambda num: num > 50, numbers)
# print(numbers)
# print(list(bigger_numbers))


# lambda function with dictionary

actors = [
  {'name':'sakib','age':34},
  {'name':'manna','age':50},
  {'name':'shabana','age':65},
  {'name':'bubly','age':30},
  ]

senior_artists = filter(lambda actor: actor['age'] > 35,actors)
junior_artists = filter(lambda actor: actor['age']<35,actors)
print(list(senior_artists))
print(list(junior_artists))