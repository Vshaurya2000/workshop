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
    for i in len(numbers):
        total = total + numbers[i]
    return sum_array
