with open('input/daytwoinput.txt', 'rt') as file:
    x = 0
    y = 0
    for line in file.readlines():
        inst = line.split()
        if inst[0] == 'forward':
            x = x + int(inst[1])
        if inst[0] == 'down':
            y = y + int(inst[1])
        if inst[0] == 'up':
            y = y - int(inst[1])
print (x*y)