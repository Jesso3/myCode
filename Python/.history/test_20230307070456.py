registers = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0}

instructions = [
    'MOV A 20',
    'MOV B 10',
    'MOV C 32',
    'MOV D 47',
    'MOV E 0',
    'MOV F 0',
    'MOV G 0',
    'MOV H 0',
    'MOV I 0',
    'MOV J 0',
    'MOV K 0',
    'MOV L 0',
    'MOV H 42',
    'ADD I 1',
    'CEQ I 42',
    'JIF -3',
    'MOV I 0',
    'CGE A H',
    'JIF 20',
    'ADD I 1',
    'ADD B -1',
    'ADD C 2',
    'MOV K 0',
    'ADD A 1',
    'ADD K 1',
    'CEQ K 10',
    'JIF 2',
    'JMP -4',
    'MOV J B',
    'MOD J 2',
    'CEQ J 0',
    'JIF 2',
    'ADD D 15',
    'JMP 2',
    'DIV D 2',
    'ADD A -5',
    'JMP -19',
    'ADD A B',
    'ADD A C',
    'ADD I -1',
    'CGE I 0',
    'JIF -3',
    'ADD A D',
    'ADD A E',
    'ADD H -10',
    'ADD E B',
    'ADD E -4',
    'ADD F E',
    'ADD G F',
    'ADD E G',
    'ADD H -1',
    'CGE H 0',
    'JIF -5',
    'ADD A F',
    'OUT A',
    'END'
]

ip = 0  # instruction pointer

while True:
    if ip >= len(instructions):
        break

    instruction = instructions[ip]
    tokens = instruction.split()

    if tokens[0] == 'ADD':
        registers[tokens[1]] += int(tokens[2])
    elif tokens[0] == 'MOD':
        registers[tokens[1]] = registers[tokens[1]] % int(tokens[2])
    elif tokens[0] == 'DIV':
        registers[tokens[1]] = registers[tokens[1]] // int(tokens[2])
    elif tokens[0] == 'MOV':
        registers[tokens[1]] = registers[tokens[2]]
    elif tokens[0] == 'JMP':
        ip += int(tokens[1])
        continue
    elif tokens[0] == 'JIF':
        if registers['__last_cmp']:
            ip += int(tokens[1])
            continue
    elif tokens[0] == 'CEQ':
        registers['__last_cmp'] = registers[tokens[1]] == registers[tokens[2]]
    elif tokens[0] == 'CGE':
        registers['__last_cmp'] = registers[tokens[1]] >= registers[tokens[2]]
    elif tokens[0] == 'OUT':
        print(registers[tokens[1]])
    elif tokens[0] == 'END':
        break

    ip += 1
