from pprint import pprint

def main():
    with open('Day3_Gear Ratios\\input.txt', 'r') as file:
        content = file.readlines()
    
    """PART 1 (uncomment for part 1)
    
    calibration_sum = 0
    for idx in range(len(content)):
        i = 0
        while i < len(content[idx]):

            if(find_number(content,idx,i) != (-1,-1)):
                num, col = find_number(content,idx, i)
                
                if(validate_number(num, idx, col, content)):
                    calibration_sum += int(num)
                
                i = col + len(num)
            
            i += 1
    print(calibration_sum)
    """

    for idx in range(len(content)):
        i = 0
        while i < len(content[idx]):
            if find_gear(content,idx,i) != (-1,-1):
                gear, col = find_gear(content,idx,i)
                verify_gear(gear, idx, col, content)

        
def find_number(content,row, col):
    if content[row][col].isdecimal():
        num = content[row][col]
        for j in range(col+1, len(content[row])):
            if content[row][j].isdecimal():
                num += content[row][j]
            else:
                col = j
                break;
        return num, col-len(num)
    else:
        return None
    

def validate_number(num, row, col, content):
    symbols = ['%', '/', '&', '-', '*', '@', '#', '+', '$', '=']
    
    # look for symbol above
    if row > 0:
        for i in range(col,col+len(num)):
            if content[row-1][i] in symbols:
                return True
        
        #look for symbol diagonal above left
        if col > 0:
            if content[row-1][col-1] in symbols:
                return True
        
        #look for symbol diagonal above right
        if (col + len(num) - 1) < (len(content[0]) - 1):
            if content[row-1][col+len(num)] in symbols:
                return True
    
    #look for symbol below
    if row < len(content) - 1:
        for i in range(col,col+len(num)):
            if content[row+1][i] in symbols:
                return True
        
        #look for symbol diagonal below left
        if col > 0:
            if content[row+1][col-1] in symbols:
                return True
        
        #look for symbol diagonal below right
        if (col + len(num) - 1) < (len(content[0]) - 1):
            if content[row+1][col+len(num)] in symbols:
                return True

    #look for symbol to the left
    if col > 0:
        if content[row][col-1] in symbols:
            return True
    
    #look for symbol to the right
    if (col + len(num) - 1) < (len(content[0]) - 1):
        if content[row][col+len(num)] in symbols:
            return True
    return False

def look_for_gear(num, row, col, content):
    gear = ['*']
    
    #look for gear below
    if row < len(content) - 1:
        for i in range(col,col+len(num)):
            if content[row+1][i] in gear:
                return True
        
        #look for gear diagonal below left
        if col > 0:
            if content[row+1][col-1] in gear:
                return True
        
        #look for gear diagonal below right
        if (col + len(num) - 1) < (len(content[0]) - 1):
            if content[row+1][col+len(num)] in gear:
                return True

    #look for gear to the left
    if col > 0:
        if content[row][col-1] in gear:
            return True
    
    #look for gear to the right
    if (col + len(num) - 1) < (len(content[0]) - 1):
        if content[row][col+len(num)] in gear:
            return True
    return False

def find_gear(content, row, col):
    if find_number(content, row, col) != (-1,-1):
        num, col = find_number(content, row, col)
        look_for_gear(num, row, col, content)
    pass

def verify_gear(gear, row, col, content):
    pass


if __name__ == "__main__":
    main()

# change look for gear to return gear coordinates
# think of an algo to not double count numbers 