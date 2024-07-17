import itertools

# the distance matrix
with open("shopping input.txt","r")as f:
    matrix = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]

# the shops we want to visit (excluding the starting and ending point)
shops = [2, 3, 4, 5,6,7,8,9,10,11,12]

# generate all possible permutations of the shops
perms = itertools.permutations(shops)

# initialize the minimum distance as infinite
min_distance = float('inf')

# iterate over all permutations
for perm in perms:
    # add the starting and ending point to the permutation
    path = [1] + list(perm) + [1]
    # calculate the total distance of the path
    distance = sum(matrix[path[i-1]-1][path[i]-1] for i in range(1, len(path)))
    # update the minimum distance if necessary
    if distance < min_distance:
        min_distance = distance

# print the minimum distance found
print(min_distance)
