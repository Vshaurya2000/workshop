grid = []
num = 1

for row in range(5):
    new_row = []  
    for col in range(5):
        new_row.append(num)
        num += 1
    grid.append(new_row)

for row in grid:
    for i in row:
        print(i, end=" ")
    print("\n")