import re
input = '555500020164048c6df0f53eab92edaf8fbdf0e7c8d597a05ff22cbcc9f17e6e'
numbers = []
numbers.append(re.sub(r'[a-zA-Z].*', '', input))
print(numbers)