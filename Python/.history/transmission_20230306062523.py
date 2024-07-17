with open("transmission input.txt","r") as f:
    data = f.read().splitlines()

grid = []
for row in data:
    parts = row.split(" ")
    for part in parts:
        print(parts, end=" ... ")
    print("end of line")