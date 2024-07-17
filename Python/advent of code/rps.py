file = open("rps input.txt")
data = file.readlines()
data = list(map(lambda s: s.strip(), data))
score = 0
'''
def winConditions(p1,p2):
    if p1 == 'A':
        if p2 == 'Y':
            return 8
        elif p2 == 'X':
            return 4
        elif p2 == 'Z':
            return 3
    if p1 == 'B':
        if p2 == 'Y':
            return 5
        elif p2 == 'X':
            return 1
        elif p2 == 'Z':
            return 9
    if p1 == 'C':
        if p2 == 'Y':
            return 2
        elif p2 == 'X':
            return 7
        elif p2 == 'Z':
            return 6
'''
def winConditions(p1,p2):
    if p1 == 'A':
        if p2 == 'Y':
            return 4
        elif p2 == 'X':
            return 3
        elif p2 == 'Z':
            return 8
    if p1 == 'B':
        if p2 == 'Y':
            return 5
        elif p2 == 'X':
            return 1
        elif p2 == 'Z':
            return 9
    if p1 == 'C':
        if p2 == 'Y':
            return 6
        elif p2 == 'X':
            return 2
        elif p2 == 'Z':
            return 7
for line in data:
  score+=winConditions(line[0],line[2])
print(score)
        