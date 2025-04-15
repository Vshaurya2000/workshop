X = input("INPUT THE NUMBER")
X = float(X)
numbers = (7,8,4,5,3)
FLAG = "NO"
for i in range(0,len(numbers),1):
    if numbers[i] == X: 
        FLAG = "YES"
        
print(FLAG)
