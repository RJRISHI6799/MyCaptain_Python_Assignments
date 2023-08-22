n = int(input("Enter the number of Fibonacci nummbers:"))

fibonacci = [0,1]

for i in range(2, n):
    next_fib = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_fib)
print("Fibonacci Sequence:", fibonacci)
