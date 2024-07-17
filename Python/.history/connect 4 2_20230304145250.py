with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

# Split the string into chunks of 49 characters
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]

# Create a 2D list with each row containing 49 single-digit integers
moves = [[int(digit) for digit in chunk] for chunk in chunks]

# Print the 2D list

print(moves[0][0])

# digits = list(str(lines))
# moves = [[0 for x in range(49)] for y in range(1000)]
# index=0
# print(moves)
# for row in range(1000):
#     for col in range(49):
#         moves[row][col]=digits[index]
#         index+=1
# num=moves[0][0]
# print(num)