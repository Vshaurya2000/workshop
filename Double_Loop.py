print("Printing 5 X 5 grid *")
for row in range(5):
   for col in range(5):
       print("*", end=" ")
   print("\n")  
    

# let num = 1
# then num+1 per tick in the loop 

print("Printing numbered 5 X 5 grid")
num = 1
for row in range(5):
    for col in range(5):
        print(num, end=" ")
        num += 1
    print("\n")

print("Printing a right angle triangle with character a")
for row in range(1,6):
   for col in range(row):
       print("a", end=" ")
   print("\n") 






