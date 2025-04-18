def sum_natural_n_number(num):
    total = 0
    for i in range(num, 0, -1):
        total += i
    return total

# num = int(input("Put a number in: "))< ------- The way to print the funtion
# result = sum_natural_n_numberl(num)
# print(result)

def add_numbers(a,b):
   return a + b
# a = int(input("Enter the first number: "))    < ----- The way to print the funtion
# b = int(input("Enter the second number: "))
# c =  add_numbers(a,b)
# print(c)

def factorial(num):
    answer = 1
    for i in range(num, 0, -1):  
        answer *= i
    return answer

# num = int(input("Enter a number: ")) < ----- The way to print the funtion
# fact = factorial(num)
# print("The factorial of", num, "is", fact)

def sum_array(numbers):
    total = 0
    for i in range(len(numbers)):  
        total += numbers[i]
    return total

# user_input = input("Enter numbers separated by spaces: ") < ----- The way to print the funtion
# numbers_list = list(map(int, user_input.split()))
# result = sum_array(numbers_list)
# print("The sum is:", result)
                  
