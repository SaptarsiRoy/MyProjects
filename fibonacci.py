def fibo(f, s, n):
    if n == 0:
        return
    t = f + s
    print(t)
    fibo(s, t, n - 1)
user_input = int(input("Enter the number of terms:"))
print("Fibonacci series")
fibo(-1, 1 ,user_input)
