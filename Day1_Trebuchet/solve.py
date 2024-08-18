
# part1
with open('Day1_Trebuchet\\input.txt', 'r') as file:
    content = file.readlines()
    calibration_values = []
    for line in content:
        calibration_value = 0
        first, last = 0, len(line) - 2 # skip the \n character
        while first <= last:
            if line[first].isdecimal():
                if line[last].isdecimal():
                    calibration_value = int(line[first]) * 10 + int(line[last])
                    break
                else:
                    last -= 1
            else:
                first += 1
        calibration_values.append(calibration_value)
print('part1: ',sum(calibration_values))

# part2

numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
           '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

with open('Day1_Trebuchet\\input.txt', 'r') as file:
    content = file.readlines()
    calibration_values = []
    for line in content:
        calibration_value = 0
        first, last = 0, len(line) - 2 # skip the \n character
        n1, n2 = -1, -1

        while first <= last:
            for num in numbers:
                # find calibration value
                if line[first:last+1].startswith(num) and n1 == -1:
                    n1 = numbers[num]
                if line[first:last+1].endswith(num) and n2 == -1:
                    n2 = numbers[num]
            
            # break if found
            if n1 != -1 and n2 != -1:
                break
            
            # move to next position if not found
            if n1 == -1:
                first += 1
            if n2 == -1:
                last -= 1
        
        calibration_value = n1 * 10 + n2
        calibration_values.append(calibration_value)
print('part2: ',sum(calibration_values))
