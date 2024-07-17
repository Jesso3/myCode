from sympy import fibonacci

i = 1
while True:
    if len(str(fibonacci(i))) >= 1000:
        print(i)
        break
    i += 1
