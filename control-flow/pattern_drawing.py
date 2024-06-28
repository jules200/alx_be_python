n = int(input("Enter the size of the pattern:"))

while n>0:
    for b in range(1, n):
        print("*", end="")
    print("*")
    n=n-1