import re
input = '2 3 1 5'
input = re.sub(r'(\d)\s+(\d)', r'\1\2', input)
print(sorted(input))
for i in range(0,len(input),2):
    pass
