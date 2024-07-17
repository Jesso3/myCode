from itertools import permutations

digits = "0123456789"
perms = list(permutations(digits))

print(''.join(perms[999999]))
