with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
numbers = []
nums = []
mod = 0
for i in data:
    k = i
    if i[:12] == "555500020164":#change with different numbers
        num = i[16:]
        value = i[14:16]
        mod = 0
        for j in range(0, len(num), 2):
            decimal_value = int(num[j:j+2], 16)
            mod += int(decimal_value)
        mod %= 256
        mod = hex(mod)
        mods = str(mod.replace('0x',''))
        if mods==value:
            numbers.append(k)
num = sorted(numbers)
for i in num:
    nums.append(i[16:])
mess = "".join(nums)
hex_pairs = [mess[i:i+2] for i in range(0, len(mess), 2)]
text = "".join([chr(int(pair, 16)) for pair in hex_pairs])
print(text)