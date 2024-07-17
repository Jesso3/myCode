'''
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 100

if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
'''

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))
terms = 10
for i in range(terms):
    print(fib(i))