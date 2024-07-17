with open("navigation_data.txt", "r") as file:
    input = file.readlines()

nums = []
for row in input:
  binary = bin(int(row))[2:]
  if binary.count('1') % 2 == 0:
      if len(binary) >= 16:
         binary = binary[:-16] + '0' + binary[-15:]
      nums.append(int(binary,2))

print(round(sum(nums) / len(nums)))


  