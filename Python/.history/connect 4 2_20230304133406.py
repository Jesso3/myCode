with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
lst = [list(map(int, line.strip().split())) for line in lines]
moves = [list(str(lines))]
games = [[' ' for col in range(49)] for row in range(1000)]
number_str = str(lines)

digit_list = [int(number_str[i:i+1]) for i in range(0, len(number_str), 49)]

# Print the list of digits
print(digit_list)
p1_moves = []
p2_moves = []
p3_moves = []
 
board = [[' ' for col in range(7)] for row in range(7)]
