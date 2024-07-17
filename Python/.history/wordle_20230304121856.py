
with open('wordle data.txt','r')as f:
    words=f.read().splitlines()

# keyless YYBBYYG
# society YGYYYBB
# phobias BBGBGBG

guesses = ["keyless","society","phobias"]
answers = ["YYBBYYG","YGYYYBB","BBGBGBG"]

# Create a list of the black and yellow letters
yellows = []
blacks = []
for n in range(0, len(answers)):
    for m in range(0, len(answers[n])):
        if answers[n][m] == "Y":
           yellows.append(guesses[n][m]) 
        if answers[n][m] == "B":
            blacks.append(guesses[n][m])

print("yellows",yellows)
print("blacks",blacks)

# check each word in our dictionary
for n in range(0, len(words)):# 0...42000
    word = words[n]
    # Check for green matches
    green_ok = True
    for m in range(0, len(word)):# 0,1,2,3,4,5,6
        letter = word[m]
        for i in range(0, len(answers)):# 0,1,2
            if answers[i][m] =="G":
                if guesses[i][m] !=letter:
                    green_ok=False
    if not green_ok: continue #restart the loop with the next word
    #print("green ok",word)
    black_ok = True
    for m in range(0, len(word)):
        letter = word[m]
        if letter in blacks:
            black_ok = False
    if not black_ok: continue
    #print("black ok", word)

    yellow_ok = True
    for m in range(0, len(yellows)):
        if yellows[m] not in word:
            yellow_ok = False
    if not yellow_ok: continue# not this word, move on

    # Passed all three checks        
    print("yellow ok",word)