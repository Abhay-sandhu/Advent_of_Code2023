with open('input.txt', 'r') as file:
    content = file.readlines()

nums = {}

for idx in range(len(content)):
    i = 0
    while i < len(content[idx]):
        if content[idx][i].isdecimal():
            num = content[idx][i]
            for j in range(i+1, len(content[idx])):
                if content[idx][j].isdecimal():
                    num += content[idx][j]
                else:
                    i = j
                    break;
            print(f"(({idx},{i-len(num)}), {num}),  ", end="")
            nums[num] = ((idx,i-len(num)), len(num))
        i += 1
    print("")

print(nums)
        
