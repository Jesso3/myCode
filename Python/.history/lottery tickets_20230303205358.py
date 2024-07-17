with open('lottery ticket input.txt', 'r') as file:
    numbers_string = file.read()
    wordList = []
    winningTicket = [12, 48, 30, 95, 15, 55, 97]
    numOfWins = 0
    for number in numbers_string.split():
        wordList.append(int(number))
    for word in wordList:
        for win in winningTicket:
            if word == win:
                numOfWins += 1
        
