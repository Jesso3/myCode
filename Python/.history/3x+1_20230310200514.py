import time
start_time = time.time()
input = 3
print(input//1)
while input > 1:
    if input % 2 == 0:
        input /= 2
    else:
        input*=3
        input+=1
    print(int(input))
print("Process finished --- %s seconds ---" % (time.time() - start_time))