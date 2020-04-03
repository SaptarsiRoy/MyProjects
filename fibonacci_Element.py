import math as m
def isPerfectSq(n):
    s = m.sqrt(n*n)
    return s == n


def isFibo(n):
    return isPerfectSq(5 * n * n + 4) or isPerfectSq(5 * n * n - 4)

user = int(input("Enter the number to check:"))
if isFibo(user):
    print("Belongs to fibonacci series")
else:
    print("Does not belong to fibonacci series")
