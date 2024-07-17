with open("debugging input.txt", "r") as f:
    lines = []
    for line in f:
        int_list = []
        values = line.strip().split()
        for item in values:
            if item.isdigit():
                int_list.append(int(item))
            else:
                int_list.append(item)
        lines.append(int_list)

registers = [0] * 12  # initialize registers with 0

ip = 0
while ip < len(lines):
    op = lines[ip][0]
    if op == "ADD":
        registers[lines[ip][1]] += registers[lines[ip][2]]
    elif op == "MOD":
        registers[lines[ip][1]] %= registers[lines[ip][2]]
    elif op == "DIV":
        registers[lines[ip][1]] //= registers[lines[ip][2]]
    elif op == "MOV":
        registers[lines[ip][1]] = registers[lines[ip][2]]
    elif op == "JMP":
        ip += lines[ip][1]
        continue
    elif op == "JIF":
        if registers[lines[ip][1]] == 0:
            ip += lines[ip][2]
            continue
    elif op == "CEQ":
        if registers[lines[ip][1]] == registers[lines[ip][2]]:
            registers[lines[ip][3]] = 1
        else:
            registers[lines[ip][3]] = 0
    elif op == "CGE":
        if registers[lines[ip][1]] >= registers[lines[ip][2]]:
            registers[lines[ip][3]] = 1
        else:
            registers[lines[ip][3]] = 0
    elif op == "OUT":
        print(registers[lines[ip][1]])
    elif op == "END":
        break
    ip += 1
