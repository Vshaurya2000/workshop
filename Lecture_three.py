#list1 = []

#list1.append(input("Put in your FAVOURITE movie"))

#list1.append(input("Put in your second favourite movie"))

#list1.append(input("Put in your third favourite movie"))
#print("Here is your choices",list1)
list1 = [7,6,6,8]
list1reverse = list1.copy()
list1reverse.reverse()
if(list1reverse == list1):
   print("This is a palindrome")
else:
   print("The following is not a palindrome",list1)