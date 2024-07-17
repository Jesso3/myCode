file = open("debugging input.txt")
data = file.readlines()
data = list(map(lambda s: s.strip(), data))

action = {}
variables = {}

for line in data:
    action = line[:3]
    print(action)