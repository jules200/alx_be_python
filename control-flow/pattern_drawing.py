n = int(input("Enter the size of the pattern:"))

for a in range(0, n):    
    for b in range(1, n):
        print("*", end="")
    print("*")