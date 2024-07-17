with open("nav_input.txt", "r") as f:
    data = f.read().splitlines()

binary = []
for row in data:
    binary.append(bin(int(row))[2:])

evens = []
bins = []
for row in binary:
    one_count = 0
    for i in row:
        if i == "1":
            one_count += 1
    if one_count % 2 == 0:
        bins.append(row)
        evens.append(int(row, 2))

ans_bins = []
ans = []
avg = 0
for i in bins:
    if len(i) >= 16:
        i = "0" + i[-15:]
    ans_bins.append(i)
    ans.append(int(i, 2))
    avg += int(i, 2)

print(evens)
print(bins)
print(ans)
print(avg / len(ans))
