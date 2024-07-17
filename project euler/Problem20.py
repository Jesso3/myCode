def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

string = str(factorial(100))
nums = []
for i in string:
    nums.append(int(i))
print(sum(nums))