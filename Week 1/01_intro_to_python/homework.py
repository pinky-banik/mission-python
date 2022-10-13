""" 
1. take three input from the user
2. add the three inputs display the sum
3. take two numbers then show the multiplication
4. take first name and last name as input and display full name
5. take 3 inputs. and output will be like:
"Hey I am ___. My age is ___. I love to eat ___."
6. take degree c and convert the temperation to F.
7. take one input display 4 time of that number.
"""

# 1. take three input from the user

a = input("first input: ")
b = input("2nd input : ")
c = input("3rd input : ")


# 2. add the three inputs display the sum

print (f"sum of the three number is:  {int(a)+int(b)+int(c)}")

# 3. take two numbers then show the multiplication
x = input("first input: ")
y = input("2nd input : ")


print(f"multiplication of the two number is : {int(x)* int(y)}")

# 4. take first name and last name as input and display full name

first_name = input("first name : ")
last_name = input("last_name : ")

print(f"full name is: {first_name} {last_name}")

# 5. take 3 inputs. and output will be like: "Hey I am ___. My age is ___. I love to eat ___."

name = input("name : ")
age = int(input ("age : "))
food = input("food : ")

print(f"Hey I am {name}. My age is {age}. I love to eat {food}.")

# 6. take degree c and convert the temperation to F.

celsius = int(input("celsius: "))

fahrenheit = celsius*(9/5) + 32

print(f"Fahrenheit valus is: {fahrenheit}")

# take one input display 4 time of that number.

number_to_be_multiplied = int(input("Number to be multiplied : "))

print(number_to_be_multiplied*number_to_be_multiplied*number_to_be_multiplied*number_to_be_multiplied)