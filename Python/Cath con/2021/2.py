original_array = [5,6,3,1,5]
shifted_array = [0 for i in range(len(original_array))]
index = -1

for i in range(len(original_array)):
  shifted_array[(i+index) % len(original_array)] = original_array[i]
  
print(shifted_array)
