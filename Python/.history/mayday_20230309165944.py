with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
numbers = []
mod = 0
for i in data:
    if i[:4] == "5555":
        if i[4:12] == "00000058": # must change with different numbers
            if i[14] == 'f':
                num = i[16:]
                value = i[14:16]
                print(value)
                mod = 0
                for i in range(0, len(num), 2):
                    decimal_value = int(num[i:i+2], 16)
                    mod += int(decimal_value)
                print(mod)
                mod %= 256
                mod = hex(mod)
                mods = str(mod.replace('0x',''))
                print((mods))
                if mods==value:
                    numbers.append(i)
print(sorted(numbers))