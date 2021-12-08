with open('input/dayoneinput.txt', 'rt') as file:
    lastvalue = False
    count = 0
    for row in file.readlines():
        currentvalue = int(row)
        if lastvalue:
            if currentvalue > lastvalue:
                count += 1
        lastvalue = currentvalue
print(count)
        
