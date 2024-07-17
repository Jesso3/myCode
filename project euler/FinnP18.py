the1s = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
the10s = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
the100s = [0, 13, 13, 15, 14, 14, 13, 15, 15, 14]
theAnomalies = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

def numOfLetters(num):
    count = 0
    if num[-4] == 0:
        if num[-2] == 1:
            subcount = theAnomalies[num[-1]]
        else:
            subcount = the1s[num[-1]] + the10s[num[-2]]
        count += subcount + the100s[num[-3]]
        if num[-1] == 0 and num[-2] == 0: #if its a perfect hundred get rid of "and"
            count -= 3
    elif num[-4] == 1:
        count = 11
    print(num,count)
    return count

def number_to_list(number):
    number_str = str(number)
    number_list = [int(digit) for digit in number_str]
    while True:
        if len(number_list) < 4:
            number_list.insert(0,0)
        else:
            break
    return number_list

totalcount = 0
currentNumber = 1
while currentNumber <= 1000:
    totalcount += numOfLetters(number_to_list(currentNumber))
    currentNumber += 1
print(totalcount)
