from Maths import *

num = int(input("Enter a number: "))
result = sum_natural_n_number(num)
print("The sum of natural numbers", result)

a = int(input("Enter the first number: "))    
b = int(input("Enter the second number: "))
c =  add_numbers(a,b)
print(c)

num = int(input("Enter a number: ")) 
fact = factorial(num)
print("The factorial of", num, "is", fact)

user_input = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, user_input.split()))
result = sum_array(numbers_list)
print("The sum is:", result)