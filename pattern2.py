n = int(input("Enter the value of n:"))
for i in range(n, 0, -1):
    output = ' '
    for j in range(i):
        output += str(i) + " "
    print(output)
