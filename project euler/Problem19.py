week_day = 2
count = 0

for y in range(1901,2001):
    for m in range(1,13):
        if m == 9 or 4 or 6 or 10:
            for d in range(1,31):
                if d == 1 and week_day == 7:
                    count += 1
                if week_day < 7:
                    week_day += 1
                else:
                    week_day = 1
        elif m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            for d in range(1,32):
                if d == 1 and week_day == 7:
                    count += 1
                if week_day < 7:
                    week_day += 1
                else:
                    week_day = 1
        elif m == 2 and y % 4 == 0:
            for d in range(1,30):
                if d == 1 and week_day == 7:
                    count += 1
                if week_day < 7:
                    week_day += 1
                else:
                    week_day = 1
        elif m == 2 and y % 4 != 0:
            for d in range(1,29):
                if d == 1 and week_day == 7:
                    count += 1
                if week_day < 7:
                    week_day += 1
                else:
                    week_day = 1
print(count)
