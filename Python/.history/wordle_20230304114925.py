
with open('wordle data.txt','r')as f:
    words=f.read().splitlines()

print(len(words))
for n in range(0, len(words)):
    word = words[n]
    for m in range(0, len(word)):
        letter = word[m]
        print(letter)