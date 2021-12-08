with open('input/daytwoinput.txt', 'rt') as file:
    x = 0
    y = 0
    aim = 0
    for line in file.readlines():
        inst = line.split()
        if inst[0] == 'forward':
            x = x + int(inst[1])
            y = y + (aim * int(inst[1]))
        if inst[0] == 'down':
            aim = aim + int(inst[1])
        if inst[0] == 'up':
            aim = aim - int(inst[1])
        print (inst[0], inst[1], aim, x, y)
print (x * y)