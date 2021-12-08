with open('input/dayoneinput.txt', 'rt') as file:
    count = 0
    list = []
    sums = []
    for row in file.readlines():
        list.append(int(row))
    for index, ele in enumerate(list):
        if index > 1:
            sums.append(list[index]+list[index-1]+list[index-2])
    lastvalue = False
    for row in sums:
        currentvalue = row
        if lastvalue:
            if currentvalue > lastvalue:
                count +=1
        lastvalue = currentvalue
print(count)