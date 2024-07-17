with open("connect 4 input.txt", "r") as f:
    lines = f.read().split()
for line in lines:
    digits = list(str(line))
    
grid = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()] # turn data into 2d list
print(grid)






# games = [[''] * 49 for _ in range(1000)]

# # for line in lines:
# #     long_number = line
# #     number_str = str(long_number)
# #     digit_list = [int(number_str[i:i+1]) for i in range(0, len(number_str))]
#     games.append(digit_list)
# print(games)