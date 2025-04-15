import random
randm = []
for i in range (0,20):
    number = (random.randint(0,100))
    randm.append(number)
Highest = max(randm)
print(randm)


highest = randm[0]  
smallest = randm[0]

for num in randm:
    if num > highest:
        highest = num
    if num < smallest:
        smallest = num

print("The biggest number in the list is", highest)
print("The smallest number in the list is", smallest)


even = []
odd = []

for digit in randm:
    
    if digit % 2 == 0:
        even.append(digit)
    else:
        odd.append(digit)


print("Even numbers:", even)
print("Odd numbers:", odd)

reversedlist = []

for i in randm:
    reversedlist.insert(0,i)

print("Here is the reversed list:", reversedlist)
    










#num1 = int(input("Enter the first number: "))

#num2 = int(input("Enter the second number: "))

#if num1 > num2:
#    print(f"The first number ({num1}) is bigger than the second number ({num2}).")
#if num1 < num2:
#    print(f"The second number ({num2}) is bigger than the first number ({num1}).")
#else:
#    print("Both numbers are equal.")