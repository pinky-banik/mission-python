numbers = [12, 45,56, 45, 12]
print(numbers)
nums = {12,45,56,45,12,89}
print(nums)

numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(77) # only addes whom is not already exists
numbers_set.add(45) # if the element is already exists then it will not add
print(numbers_set)
print (len(numbers_set))