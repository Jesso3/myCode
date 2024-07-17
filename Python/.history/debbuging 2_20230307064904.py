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
