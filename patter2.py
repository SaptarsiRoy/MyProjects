n = int(input("Enter the value of n:"))
for i in range(n):
    output = ' '
    for j in range(i-1, 0, -1):
        output += j
    print(output)
