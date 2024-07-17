with open("heat input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
# grid = [[0 for x in range(10)] for y in range(10)]
# print(data)
# # for row in data:
# #     print(row)
# ri = 0  
# for i in range(len(data)):
#     for row in range(data[ri][0],data[ri][2]):
#         for col in range(data[ri][1],data[ri][3]):
#             grid[row][col]="x"
#     ri+=1
# for row in grid:
#     print(row)
for row in data:
    print(row)
print(data[0][0])