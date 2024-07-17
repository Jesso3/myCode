with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
    # Create an empty 1000 by 49 2D list
games = [[None] * 49 for _ in range(1000)]

for line in lines:
    long_number = line
    number_str = str(long_number)
    digit_list = [int(number_str[i:i+1]) for i in range(0, len(number_str))]
    games.append(digit_list)
print(games)