with (open("/Users/jesse/Desktop/python_code/project euler/problem18.txt","r")) as file:
    lines = file.readlines()
triangle = [list(map(int, line.split())) for line in lines]

for row in range(len(triangle) - 2, -1, -1):
    for col in range(len(triangle[row])):
        # Add the larger of the two adjacent numbers in the row below
        triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

# The top number now contains the maximum total
max_total = triangle[0][0]

# Print the result
print(max_total)