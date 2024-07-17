lines = []
intList = []
with open("debugging input.txt", "r") as f:
    for line in f:
        values = line.strip().split()
        for item in values:
            if item.isdigit():
                intList.append(int(item))
            else:
                intList.append(item)
        lines.append(intList)
        intList = []
for row in lines:
    print(row)
instructions = {
    "ADD": lambda target, source: target + source,
    "MOD": lambda target, source: target % source,
    "DIV": lambda target, source: target // source,
    "MOV": lambda target, source: source,
    "JMP": lambda source: None,
    "JIF": lambda source, jump: jump if source else None,
    "CEQ": lambda source1, source2: source1 == source2,
    "CGE": lambda source1, source2: source1 >= source2,
    "OUT": lambda source: print(source),
    "END": lambda: exit()
}
