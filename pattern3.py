n = int(input("Enter the number of rows:"))
for i in range(1, n+1):
    output = ""
    for j in range(1, i+1):
        output += str(j)
    print(output)
