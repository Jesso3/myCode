with open('mayday_input.txt','r')as f:
    data=f.read().splitlines()
numbers = []
nums = []
mod = 0
for i in data:
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
            numbers.append(i)
num = sorted(numbers)
for i in num:
    nums.append(i[16:])
mess = "".join(nums)
text = bytearray.fromhex(mess).decode()
print(text)