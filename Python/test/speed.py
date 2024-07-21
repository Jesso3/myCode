import time

# Start the timer
start_time = time.time()

# Print 1 million empty strings
for i in range(1000000000):
    print("", end="")

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Time taken to print 1 million empty strings: {elapsed_time} seconds")
