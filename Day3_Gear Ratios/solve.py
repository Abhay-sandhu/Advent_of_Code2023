from pprint import pprint

def main():
    with open('input.txt', 'r') as file:
        content = file.readlines()
    
    calibration_sum = 0
    for idx in range(len(content)):
        i = 0
        while i < len(content[idx]):

            if(find_number(content[idx],i) != (-1,-1)):
                num, col = find_number(content[idx], i)
                
                if(validate_number(num, idx, col, content)):
                    calibration_sum += int(num)
                
                i = col + len(num)
            
            i += 1
    print(calibration_sum)
    
        
def find_number(line, i):
    if line[i].isdecimal():
        num = line[i]
        for j in range(i+1, len(line)):
            if line[j].isdecimal():
                num += line[j]
            else:
                i = j
                break;
        return num, i-len(num)
    else:
        return -1, -1
    

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

if __name__ == "__main__":
    main()