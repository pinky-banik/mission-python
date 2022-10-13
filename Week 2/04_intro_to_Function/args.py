def add(num1,num2):
  total = num1 + num2
  print(num1,num2)
  return total

# result = add(12,14)
# result = add(num1=15,num2=15)


def multiply (num1,num2 =1):
  result = (num1*num2)
  return result

output = multiply(45,2)
# print(output)


# tuple
def multiply2(*numbers): # here * is args
  result = 1
  for num in numbers:
    result = result * num
  return result
final_result = multiply2(12,2,3,5)
print(final_result)
