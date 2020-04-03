#function for swapping
def swap(s):
    i = 0
    j = len(s)
    for item in s:
        tmp = s[i]
        s[i] = s[j - 1]
        s[j - 1] = tmp
        i += 1
        j -= 1
        if i >= j:
            break
    return s


#calling above function
x = input("Enter numbers:\n")
s = []
for item in x:
    s.append(item)
new_s = swap(s)
print("\n\nThe numbers are")
for item in new_s:
    print(item)
