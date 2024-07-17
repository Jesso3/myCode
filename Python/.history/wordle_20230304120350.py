
with open('wordle data.txt','r')as f:
    words=f.read().splitlines()

guesses = ["hapless","jackpot","fullest"]
answers = ["GBYYYBB","BBBBYBB","YYGYYBB"]

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

# for n in range(0, len(words)):# 0...42000
#     word = words[n]
#     green_ok = True
#     for m in range(0, len(word)):# 0,1,2,3,4,5,6
#         letter = word[m]
#         for i in range(0, len(answers)):# 0,1,2
#             if answers[i][m] =="G":
#                 if guesses[i][m] !=letter:
#                     green_ok=False
#     if not green_ok: continue #restart the loop with the next word
#     yellow_ok = True
#     for m in range(0,len(word)):
#         letter = word[m]
#         if letter not in yellows:
#             yellow_ok = False